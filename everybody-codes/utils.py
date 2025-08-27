#!/usr/bin/env python3
"""
Simple Everybody Codes API utilities

Usage:
    from utils import get_data, submit
    
    text = get_data(event=1, quest=1, part=1)
    answer = 123
    submit(answer, event=1, quest=1, part=1)
"""

import os
import json
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
from typing import Optional
from pathlib import Path


class _EverybodyCodesAPI:
    """Internal API client for Everybody Codes."""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
        })
        
        # Set up config directory
        self.config_dir = Path.home() / '.config' / 'ecd'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        # Load token and user info
        self._load_token()
        self._load_user_info()
        
        # Cache
        self._aes_keys_cache = {}
    
    def _load_token(self):
        """Load token from ~/.config/ecd/token file."""
        token_file = self.config_dir / 'token'
        if token_file.exists():
            token = token_file.read_text().strip()
            self.session.cookies.set('everybody-codes', token, domain='everybody.codes')
    
    def _load_user_info(self):
        """Load or create user info from ~/.config/ecd/user.json."""
        user_file = self.config_dir / 'user.json'
        
        if user_file.exists():
            try:
                self.user_info = json.loads(user_file.read_text())
                self.user_id = self.user_info.get('id')
                self.user_seed = self.user_info.get('seed')
            except:
                self.user_info = {}
                self.user_id = None
                self.user_seed = None
        else:
            self.user_info = {}
            self.user_id = None
            self.user_seed = None
    
    def _save_user_info(self):
        """Save user info to ~/.config/ecd/user.json."""
        user_file = self.config_dir / 'user.json'
        user_file.write_text(json.dumps(self.user_info, indent=2))
    
    def _get_user_cache_dir(self) -> Optional[Path]:
        """Get the user-specific cache directory."""
        if not self.user_id:
            return None
        cache_dir = self.config_dir / str(self.user_id)
        cache_dir.mkdir(exist_ok=True)
        return cache_dir
    
    def _get_cache_file(self, category: str, key: str) -> Optional[Path]:
        """Get path to a cache file in user directory."""
        cache_dir = self._get_user_cache_dir()
        if not cache_dir:
            return None
        return cache_dir / f'{category}_{key}.json'
    
    def _load_cache_file(self, category: str, key: str) -> Optional[dict]:
        """Load cache from file."""
        cache_file = self._get_cache_file(category, key)
        if cache_file and cache_file.exists():
            try:
                return json.loads(cache_file.read_text())
            except:
                return None
        return None
    
    def _save_cache_file(self, category: str, key: str, data: dict):
        """Save cache to file."""
        cache_file = self._get_cache_file(category, key)
        if cache_file:
            cache_file.write_text(json.dumps(data, indent=2))
    
    def get_user_info(self) -> Optional[dict]:
        """Get user information from API and cache it."""
        if self.user_seed:
            return self.user_info
        
        try:
            response = self.session.get("https://everybody.codes/api/user/me")
            response.raise_for_status()
            data = response.json()
            
            self.user_info = data
            self.user_id = data.get('id')
            self.user_seed = data.get('seed')
            
            self._save_user_info()
            return self.user_info
        except:
            return None
    
    def decrypt_input(self, key: str, encrypted_text: str) -> Optional[str]:
        """Decrypt input using AES-CBC."""
        try:
            encrypted_bytes = binascii.unhexlify(encrypted_text)
            key_bytes = key.encode('utf-8')
            iv_bytes = key[:16].encode('utf-8')
            
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
            decrypted_bytes = cipher.decrypt(encrypted_bytes)
            decrypted_text = unpad(decrypted_bytes, AES.block_size)
            
            return decrypted_text.decode('utf-8')
        except:
            return None
    
    def get_aes_keys(self, event: str, quest: int) -> dict:
        """Get AES keys for all parts of a quest."""
        cache_key = f"{event}_{quest}"
        
        if cache_key not in self._aes_keys_cache:
            # Try to load from cache first
            cached_keys = self._load_cache_file('aes_keys', cache_key)
            if cached_keys:
                self._aes_keys_cache[cache_key] = cached_keys
            else:
                try:
                    url = f"https://everybody.codes/api/event/{event}/quest/{quest}"
                    response = self.session.get(url)
                    response.raise_for_status()
                    data = response.json()
                    
                    keys = {}
                    for p in [1, 2, 3]:
                        part_key = data.get(f"key{p}", {})
                        if part_key:
                            keys[p] = part_key
                    
                    self._aes_keys_cache[cache_key] = keys
                    
                    # Save to cache
                    self._save_cache_file('aes_keys', cache_key, keys)
                except:
                    self._aes_keys_cache[cache_key] = {}
        
        return self._aes_keys_cache[cache_key]
    
    def get_encrypted_input(self, event: str, quest: int, part: int) -> Optional[str]:
        """Get encrypted input for a specific part."""
        if not self.user_seed:
            return None
        
        cache_key = f"{event}_{quest}_{part}"
        
        # Try to load from cache first
        cached_data = self._load_cache_file('encrypted_inputs', cache_key)
        if cached_data:
            return cached_data.get('data')
        
        try:
            url = f"https://everybody-codes.b-cdn.net/assets/{event}/{quest}/input/{self.user_seed}.json"
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            
            encrypted_input = data.get(str(part))
            if encrypted_input:
                # Save to cache
                self._save_cache_file('encrypted_inputs', cache_key, {
                    'data': encrypted_input,
                    'timestamp': str(response.headers.get('date', ''))
                })
            
            return encrypted_input
        except:
            return None
    
    def submit_answer(self, answer: str, event: str, quest: int, part: int) -> bool:
        """Submit an answer."""
        cache_key = f"{event}_{quest}_{part}_{answer}"
        
        # Check if we've already submitted this answer
        cached_result = self._load_cache_file('submissions', cache_key)
        if cached_result:
            if not cached_result['correct']:
                print(f"Not submitting {answer} again. Previous response: {cached_result['message']}")
                return False
        
        try:
            url = f"https://everybody.codes/api/event/{event}/quest/{quest}/part/{part}/answer"
            data = {"answer": str(answer)}
            response = self.session.post(url, json=data)
            response.raise_for_status()
            result = response.json()
            
            # Cache the result
            self._save_cache_file('submissions', cache_key, {
                'correct': result.get('correct', False),
                'message': result.get('message', ''),
                'timestamp': str(response.headers.get('date', ''))
            })
            
            return result.get('correct', False)
        except Exception as e:
            # Cache failed attempts too
            self._save_cache_file('submissions', cache_key, {
                'correct': False,
                'message': f"Request failed: {str(e)}",
                'timestamp': ''
            })
            return False


# Global API instance
_api = _EverybodyCodesAPI()


def get_data(event: int, quest: int, part: int) -> str:
    """
    Get input data for a challenge part.
    
    Args:
        event: Event number (e.g., 2024)
        quest: Quest number (e.g., 1)
        part: Part number (1, 2, or 3)
    
    Returns:
        The decrypted input text
    
    Raises:
        Exception: If data cannot be retrieved or decrypted
    """
    event_str = str(event)
    cache_key = f"{event}_{quest}_{part}"
    
    # Check decrypted input cache first
    cached_data = _api._load_cache_file('decrypted_inputs', cache_key)
    if cached_data:
        return cached_data.get('data')
    
    # Get encrypted input
    encrypted_input = _api.get_encrypted_input(event_str, quest, part)
    if not encrypted_input:
        raise Exception(f"Could not fetch encrypted input for event={event}, quest={quest}, part={part}")
    
    # Get AES keys
    aes_keys = _api.get_aes_keys(event_str, quest)
    aes_key = aes_keys.get(part)
    if not aes_key:
        raise Exception(f"Could not fetch AES key for event={event}, quest={quest}, part={part}")
    
    # Decrypt input
    decrypted_input = _api.decrypt_input(aes_key, encrypted_input)
    if not decrypted_input:
        raise Exception(f"Could not decrypt input for event={event}, quest={quest}, part={part}")
    
    # Cache the decrypted result
    _api._save_cache_file('decrypted_inputs', cache_key, {
        'data': decrypted_input,
        'timestamp': ''
    })
    
    return decrypted_input


def submit(answer, event: int, quest: int, part: int) -> bool:
    """
    Submit an answer for a challenge part.
    
    Args:
        answer: The answer to submit
        event: Event number (e.g., 2024)
        quest: Quest number (e.g., 1)
        part: Part number (1, 2, or 3)
    
    Returns:
        True if submission was successful, False otherwise
    """
    event_str = str(event)
    return _api.submit_answer(str(answer), event_str, quest, part)


def check_auth() -> bool:
    """
    Check if authentication is working.
    
    Returns:
        True if authenticated, False otherwise
    """
    return _api.get_user_info() is not None


def clear_cache():
    """Clear all cached data."""
    cache_dir = _api._get_user_cache_dir()
    if cache_dir:
        for cache_file in cache_dir.glob('*.json'):
            cache_file.unlink()
    
    _api._aes_keys_cache = {}


def get_config_dir() -> Path:
    """
    Get the configuration directory path.
    
    Returns:
        Path to the ~/.config/ecd/ directory
    """
    return _api.config_dir


def get_user_cache_dir() -> Optional[Path]:
    """
    Get the user-specific cache directory path.
    
    Returns:
        Path to the ~/.config/ecd/{user_id}/ directory, or None if not authenticated
    """
    return _api._get_user_cache_dir()

