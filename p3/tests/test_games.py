from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_nim():
    def sat(moves: List[List[int]], initial_state=[5, 9, 3, 11, 18, 25, 1, 2, 4, 1]):
    
        def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
            vals = sorted(state, reverse=True)
            i_largest = state.index(vals[0])  # largest heap
            state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie
    
        state = initial_state[:]  # copy
        for i, n in moves:
            assert 0 < n <= state[i], "Illegal move"
            state[i] -= n
            if set(state) == {0}:
                return True  # you won!
            assert any(state), "You lost!"
            bot_move()

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nim_1():
    def sat(moves: List[List[int]], initial_state=[4, 1, 8, 0, 5, 9, 2, 0]):
    
        def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
            vals = sorted(state, reverse=True)
            i_largest = state.index(vals[0])  # largest heap
            state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie
    
        state = initial_state[:]  # copy
        for i, n in moves:
            assert 0 < n <= state[i], "Illegal move"
            state[i] -= n
            if set(state) == {0}:
                return True  # you won!
            assert any(state), "You lost!"
            bot_move()

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nim_2():
    def sat(moves: List[List[int]], initial_state=[2, 5, 3, 7, 0]):
    
        def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
            vals = sorted(state, reverse=True)
            i_largest = state.index(vals[0])  # largest heap
            state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie
    
        state = initial_state[:]  # copy
        for i, n in moves:
            assert 0 < n <= state[i], "Illegal move"
            state[i] -= n
            if set(state) == {0}:
                return True  # you won!
            assert any(state), "You lost!"
            bot_move()

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nim_3():
    def sat(moves: List[List[int]], initial_state=[3, 3, 2, 2, 3, 8]):
    
        def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
            vals = sorted(state, reverse=True)
            i_largest = state.index(vals[0])  # largest heap
            state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie
    
        state = initial_state[:]  # copy
        for i, n in moves:
            assert 0 < n <= state[i], "Illegal move"
            state[i] -= n
            if set(state) == {0}:
                return True  # you won!
            assert any(state), "You lost!"
            bot_move()

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nim_4():
    def sat(moves: List[List[int]], initial_state=[5, 8, 3, 0]):
    
        def bot_move():  # bot takes objects from the largest heap to make it match the second largest heap
            vals = sorted(state, reverse=True)
            i_largest = state.index(vals[0])  # largest heap
            state[i_largest] -= max(vals[0] - vals[1], 1)  # must take some, take 1 in case of tie
    
        state = initial_state[:]  # copy
        for i, n in moves:
            assert 0 < n <= state[i], "Illegal move"
            state[i] -= n
            if set(state) == {0}:
                return True  # you won!
            assert any(state), "You lost!"
            bot_move()

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_mastermind():
    def sat(transcripts: List[str], max_moves=10):
        COLORS = "ABCDEF"
    
        def helper(secret: str, transcript=""):
            if transcript.count("\n") == max_moves:
                return False
            guess = min([t for t in transcripts if t.startswith(transcript)], key=len)[-4:]
            if guess == secret:
                return True
            assert all(g in COLORS for g in guess)
            perfect = {c: sum([g == s == c for g, s in zip(guess, secret)]) for c in COLORS}
            almost = sum(min(guess.count(c), secret.count(c)) - perfect[c] for c in COLORS)
            return helper(secret, transcript + f"{guess} {sum(perfect.values())}{almost}\n")
    
        return all(helper(r + s + t + u) for r in COLORS for s in COLORS for t in COLORS for u in COLORS)

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_mastermind_1():
    def sat(transcripts: List[str], max_moves=8):
        COLORS = "ABCDEF"
    
        def helper(secret: str, transcript=""):
            if transcript.count("\n") == max_moves:
                return False
            guess = min([t for t in transcripts if t.startswith(transcript)], key=len)[-4:]
            if guess == secret:
                return True
            assert all(g in COLORS for g in guess)
            perfect = {c: sum([g == s == c for g, s in zip(guess, secret)]) for c in COLORS}
            almost = sum(min(guess.count(c), secret.count(c)) - perfect[c] for c in COLORS)
            return helper(secret, transcript + f"{guess} {sum(perfect.values())}{almost}\n")
    
        return all(helper(r + s + t + u) for r in COLORS for s in COLORS for t in COLORS for u in COLORS)

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_mastermind_2():
    def sat(transcripts: List[str], max_moves=6):
        COLORS = "ABCDEF"
    
        def helper(secret: str, transcript=""):
            if transcript.count("\n") == max_moves:
                return False
            guess = min([t for t in transcripts if t.startswith(transcript)], key=len)[-4:]
            if guess == secret:
                return True
            assert all(g in COLORS for g in guess)
            perfect = {c: sum([g == s == c for g, s in zip(guess, secret)]) for c in COLORS}
            almost = sum(min(guess.count(c), secret.count(c)) - perfect[c] for c in COLORS)
            return helper(secret, transcript + f"{guess} {sum(perfect.values())}{almost}\n")
    
        return all(helper(r + s + t + u) for r in COLORS for s in COLORS for t in COLORS for u in COLORS)

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_tictactoex():
    def sat(good_boards: List[str]):
        board_bit_reps = {tuple(sum(1 << i for i in range(9) if b[i] == c) for c in "XO") for b in good_boards}
        win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]
    
        def tie(x, o):  # returns True if X has a forced tie/win assuming it's X's turn to move.
            x |= 1 << [i for i in range(9) if (x | (1 << i), o) in board_bit_reps][0]
            return not win[o] and (win[x] or all((x | o) & (1 << i) or tie(x, o | (1 << i)) for i in range(9)))
    
        return tie(0, 0)

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_tictactoeo():
    def sat(good_boards: List[str]):
        board_bit_reps = {tuple(sum(1 << i for i in range(9) if b[i] == c) for c in "XO") for b in good_boards}
        win = [any(i & w == w for w in [7, 56, 73, 84, 146, 273, 292, 448]) for i in range(512)]
    
        def tie(x, o):  # returns True if O has a forced tie/win. It's O's turn to move.
            if o | x != 511:  # complete board
                o |= 1 << [i for i in range(9) if (x, o | (1 << i)) in board_bit_reps][0]
            return not win[x] and (win[o] or all((x | o) & (1 << i) or tie(x | (1 << i), o) for i in range(9)))
    
        return all(tie(1 << i, 0) for i in range(9))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_rockpaperscissors():
    def sat(probs: List[float]):
        assert len(probs) == 3 and abs(sum(probs) - 1) < 1e-6
        return max(probs[(i + 2) % 3] - probs[(i + 1) % 3] for i in range(3)) < 1e-6

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nash():
    def sat(strategies: List[List[float]], A=[[1.0, -1.0], [-1.3, 0.8]], B=[[-0.9, 1.1], [0.7, -0.8]], eps=0.01):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nash_1():
    def sat(strategies: List[List[float]], A=[[0.14738177495578275, 0.747980019825271, 0.1051232435961047, 0.46907581621423977, 0.4706551623263341, 0.9062661953318937], [0.12988166612252583, 0.890441435875433, 0.15190125502216845, 0.0251552990265973, 0.32734850066506815, 0.3591430990509836], [0.9425550188084191, 0.08611212072450258, 0.783624348822126, 0.5349936815267257, 0.10270055080436169, 0.009590499808168174], [0.6380601343485022, 0.2218383099094161, 0.6868257338754123, 0.806638752054053, 0.9018561622314694, 0.7590395566591508], [0.6859264269381581, 0.3699302620070518, 0.9942148381089508, 0.8903935289162987, 0.674293629800702, 0.11410994407146158], [0.019262410240239114, 0.35560181353997367, 0.8517917641156626, 0.3074607746901762, 0.9261733304770997, 0.15224796120543604], [0.03366324617275729, 0.8709614609040649, 0.5849217229245649, 0.6379408604095658, 0.07001731910881204, 0.9582581413742493], [0.4142207195937342, 0.3193135769930635, 0.10706268323342383, 0.942046924893307, 0.9143451786836865, 0.701950437311744], [0.5179763142759984, 0.6412718009580387, 0.20022057700520002, 0.5942457297156203, 0.19646377673223914, 0.1351944216925801]], B=[[0.6516235984777713, 0.6123203626800926, 0.6186872023667903, 0.3853596754503974, 0.1073381662525007, 0.1291386906927786], [0.4925608374781314, 0.6308638606801343, 0.9530950453320264, 0.19706903321155278, 0.24184190603658184, 0.5045244344435803], [0.441426258818589, 0.38377342845027484, 0.012225023944992808, 0.891576455082707, 0.7733199528680031, 0.5559723587618317], [0.40823234393591534, 0.3751689897312942, 0.9735593124687937, 0.9428257869910855, 0.8271844491151399, 0.9685273237161491], [0.4832145692461641, 0.5635754453674369, 0.35994676263243286, 0.7815677383683111, 0.9809479850913646, 0.2808093367857648], [0.7473188591890239, 0.12760325771253167, 0.6709148257444112, 0.6960324705687125, 0.9742301280874588, 0.5061403432364218], [0.5512441627071583, 0.24752179828917065, 0.8112753285511846, 0.31333832922799887, 0.6811740304141864, 0.9411639311639899], [0.7477089685706007, 0.2569950106729836, 0.5041394572889569, 0.10948936347507965, 0.6055289733960375, 0.5733220923473799], [0.6810018730369142, 0.7452579755751384, 0.5448601672849144, 0.6414658827186077, 0.8050401801463669, 0.729851403010736]], eps=0.1):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nash_2():
    def sat(strategies: List[List[float]], A=[[0.4934719584926307, 0.05664225783974475, 0.4878391988801185, 0.6983347656105304, 0.7903235569844771], [0.9209179850842271, 0.6945169729870889, 0.985586605726519, 0.03611807745215567, 0.07791862369265457]], B=[[0.5723776540419043, 0.3177494964308457, 0.03283373751184504, 0.960932861317398, 0.3843454398162133], [0.7415658068058613, 0.4423455643375954, 0.9314198922910875, 0.937956471095574, 0.6337568371723998]], eps=0.01):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nash_3():
    def sat(strategies: List[List[float]], A=[[0.8589758630993106, 0.7749919744562254, 0.18371378758390233, 0.28034839679007295, 0.18276337511723684, 0.5173168267432149], [0.535972149604936, 0.6860082336427572, 0.8154412069051551, 0.02442129105356694, 0.1349312146704914, 0.7530215223132398], [0.3519956107153608, 0.9660103168436817, 0.10172694662400983, 0.7254690944575098, 0.8254057287673647, 0.3189629245726713], [0.5725690579346981, 0.1589108703965545, 0.01688986355891453, 0.3074319760280675, 0.4584643560452394, 0.5853201363256517], [0.6489314270374363, 0.6347169492821729, 0.18348768635443546, 0.5731694328630751, 0.6566567470060826, 0.8039403838540958], [0.4917243999522437, 0.16144631954506772, 0.04044367374900226, 0.09502214062659131, 0.8738947440998662, 0.6114058437094053], [0.1967023709822303, 0.29782628261932154, 0.058285139123036234, 0.6302740689117773, 0.33364400882000855, 0.5776389301631869], [0.6777544316258026, 0.6724283041374894, 0.9798391425483743, 0.8838381708326536, 0.6667218181098736, 0.34481925547433623], [0.5958711406283824, 0.44387553450142214, 0.6668717494447683, 0.25986773196752133, 0.8873567554013287, 0.4374385442834563]], B=[[0.6509157248335261, 0.47969567636489663, 0.7175654058769987, 0.8305604678011964, 0.11420347930129515, 0.8401333925076142], [0.8690852438876666, 0.8127345690587251, 0.316832083958, 0.9589533790230425, 0.6983255500551921, 0.4492765771156503], [0.7058401433380928, 0.007340378623609478, 0.5423001137088079, 0.2066909384280825, 0.3317417420195775, 0.003203599551001912], [0.4887994419103735, 0.4082867953539032, 0.3605910405209234, 0.19354666101193807, 0.3116629413961449, 0.9698417812464528], [0.30623970889248353, 0.8377553335650854, 0.7624220111189529, 0.22826919233755616, 0.3832245488487954, 0.11387974071378948], [0.8818032772640031, 0.24028195971823052, 0.8834992573768841, 0.9883007945834051, 0.7024933884432355, 0.7617988546407181], [0.9160905473729156, 0.6927856066612084, 0.6159687601776853, 0.15074396336216966, 0.7764252875888226, 0.3459191304782905], [0.9991431698755587, 0.32389039099370287, 0.8354695347283115, 0.51319161530113, 0.5229921145906276, 0.7690459477032934], [0.7591967670432632, 0.23382636010443625, 0.26521035423368, 0.8577953561722641, 0.020432130142500116, 0.019755815416500178]], eps=0.1):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_nash_4():
    def sat(strategies: List[List[float]], A=[[0.5753373910044396, 0.883286704506171, 0.14098419242590676, 0.0796482735170555, 0.28053511699815137, 0.4802587237433614, 0.7927565741942321, 0.10486790699611082], [0.674897469149739, 0.5526354958094333, 0.14126552040252316, 0.8176885681560745, 0.5950057513195114, 0.9394498004514682, 0.9974412293717752, 0.31785998202168364], [0.8551492483900579, 0.0873581901597057, 0.7058504781434135, 0.8614481823894408, 0.774002479389802, 0.5194163269795865, 0.8839947283493329, 0.4796849532033839], [0.24669121918914239, 0.9192009909426845, 0.22533689422848313, 0.42231986064003346, 0.8524917527913644, 0.3217815290765713, 0.13012568628724053, 0.08517580086974996], [0.6708003793106111, 0.9370021425919828, 0.956981559137809, 0.48294825852969425, 0.09451427192867867, 0.958711015678715, 0.13874285709747414, 0.17240487357189138], [0.6862479923713413, 0.40988185301904767, 0.7232258320050972, 0.12156129874113497, 0.4137204968814412, 0.43096712555208105, 0.9673727161037606, 0.9554536674896775], [0.2645245766573283, 0.16353379162998616, 0.8208329137057697, 0.24945486012929086, 0.19060921538692044, 0.6886849242360286, 0.6513544853108113, 0.13898253443118158], [0.8399423196728664, 0.5583901386668076, 0.05055384968867316, 0.272512815876485, 0.4706764309925491, 0.9920874820129374, 0.11006687231735834, 0.6003338823254668]], B=[[0.8661101149166154, 0.5041424261188884, 0.654530488206357, 0.842287965510257, 0.5418722524658692, 0.615317049155107, 0.2474305118268787, 0.802249852604974], [0.17399126319302805, 0.37286827574250436, 0.9025123265462714, 0.6302774019777034, 0.6096954531215514, 0.14282756248667317, 0.5039665393854678, 0.5053857713064859], [0.08645764165911696, 0.34639849481946294, 0.4003286765389642, 0.8522825407634552, 0.38924375107949505, 0.13708630962779877, 0.09413370097193263, 0.024977157717289145], [0.18665183173707744, 0.08210966062569414, 0.8906028770829486, 0.9292380534706237, 0.3432700204525524, 0.03791015448620483, 0.23701146631134296, 0.5236370615896554], [0.4158240648499627, 0.620309795706114, 0.6606023798050246, 0.7581954943445194, 0.9399309644265448, 0.6640739757418763, 0.5470483802958659, 0.3881528058493644], [0.8452380694038372, 0.7687623496765781, 0.22422282300746144, 0.03236167241305821, 0.1113965246318579, 0.4589759506900418, 0.8415359432321317, 0.27521377409486303], [0.6582156349227984, 0.9988816473957544, 0.4901663751981855, 0.3788210957458895, 0.455713995042737, 0.04960398762882756, 0.16850674065572013, 0.6202540021741917], [0.7515673992699056, 0.6867547828670959, 0.038529441293790434, 0.9995963277046196, 0.15577904716257307, 0.2596640500026437, 0.76139213514593, 0.5065163836406463]], eps=0.01):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert len(B) == m and all(len(row) == n for row in A + B), "inputs are a bimatrix game"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        w = sum(B[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(B[i][j] * p[i] for i in range(m)) <= w + eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_zerosum():
    def sat(strategies: List[List[float]], A=[[0.0, -0.5, 1.0], [0.75, 0.0, -1.0], [-1.0, 0.4, 0.0]], eps=0.01):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert all(len(row) == n for row in A), "inputs are a matrix"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_zerosum_1():
    def sat(strategies: List[List[float]], A=[[0.5303369225581901, 0.4458248560112187, 0.47857713121903245], [0.07696760921779966, 0.40492093882513336, 0.8351857615090292]], eps=0.5):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert all(len(row) == n for row in A), "inputs are a matrix"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_zerosum_2():
    def sat(strategies: List[List[float]], A=[[0.8737161029595927, 0.3380931327691771, 0.20525289813478453, 0.9772812942597162, 0.6011469499669913, 0.5657635078441663, 0.007362594660960342, 0.5523386597843655, 0.06548815570594102], [0.8440989957774637, 0.11456946368545384, 0.6266416865322296, 0.6112942108318355, 0.15090892170912606, 0.19181369635746925, 0.23558304486799253, 0.08883158381322309, 0.5626427070785186], [0.5990766112287766, 0.16770300013300976, 0.7790082288508813, 0.8213933806929374, 0.8409107317631046, 0.32215242243482034, 0.04927911582647726, 0.18589922022642869, 0.4416673076660764]], eps=0.1):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert all(len(row) == n for row in A), "inputs are a matrix"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_zerosum_3():
    def sat(strategies: List[List[float]], A=[[0.35120738216503444, 0.6305426964442432, 0.09361690123750299, 0.17215263015782456, 0.3569473010721259], [0.9341169088059124, 0.43769720086284414, 0.35911118735479475, 0.37956863261812823, 0.9170151449695092]], eps=0.1):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert all(len(row) == n for row in A), "inputs are a matrix"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))

    assert sat(...)


@pytest.mark.skip(reason="not implemented yet")
def test_zerosum_4():
    def sat(strategies: List[List[float]], A=[[0.6637255179009651, 0.9756262037263238, 0.4926064602986052, 0.4097654368373934, 0.9284930704872523], [0.21641001481296873, 0.3381822244340763, 0.10113277325663139, 0.867285215856176, 0.27100572371021947], [0.7831143244052009, 0.6045743236145783, 0.10582868480749341, 0.5591604978434377, 0.27602687543748194], [0.8431935916393734, 0.09227518008541435, 0.06352450108543961, 0.13377427705288458, 0.8928593671227156], [0.15573895145866545, 0.3897235344943152, 0.5095156356106815, 0.25893802778092634, 0.4730747656010391]], eps=0.1):
        m, n = len(A), len(A[0])
        p, q = strategies
        assert all(len(row) == n for row in A), "inputs are a matrix"
        assert len(p) == m and len(q) == n, "solution is a pair of strategies"
        assert sum(p) == sum(q) == 1.0 and min(p + q) >= 0.0, "strategies must be non-negative and sum to 1"
        v = sum(A[i][j] * p[i] * q[j] for i in range(m) for j in range(n))
        return (all(sum(A[i][j] * q[j] for j in range(n)) <= v + eps for i in range(m)) and
                all(sum(A[i][j] * p[i] for i in range(m)) >= v - eps for j in range(n)))

    assert sat(...)
