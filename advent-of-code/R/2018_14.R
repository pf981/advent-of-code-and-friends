library(tidyverse)


score <- function(after_n_recipes) {
  recipes <- c(3, 7)
  elf1_i <- 1
  elf2_i <- 2

  while (length(recipes) < after_n_recipes + 1 + 10) {
    # message(glue::glue("{elf1_i}, {elf2_i}: {str_c(recipes, collapse = ' ')}"))
    recipe_sum <- recipes[elf1_i] + recipes[elf2_i]
    new_recipe1 <- if (recipe_sum >= 10) (recipe_sum %/% 10) %% 10
    new_recipe2 <- recipe_sum %% 10

    recipes <- c(recipes, new_recipe1, new_recipe2)

    elf1_i <- elf1_i + recipes[elf1_i] + 1
    while (elf1_i > length(recipes)) elf1_i <- elf1_i - length(recipes)
    elf2_i <- elf2_i + recipes[elf2_i] + 1
    while (elf2_i > length(recipes)) elf2_i <- elf2_i - length(recipes)
  }

  str_c(recipes[seq(from = after_n_recipes + 1, length.out = 10)], collapse = "")
}

answer <- score(input)
answer

# This was too slow

# n_recipes <- function(score) {
#   recipes <- c(3, 7)
#   score <- as.character(score)
#   elf1_i <- 1
#   elf2_i <- 2
  
#   repeat {
#     # message(glue::glue("{elf1_i}, {elf2_i}: {str_c(recipes, collapse = ' ')}"))
#     recipe_sum <- recipes[elf1_i] + recipes[elf2_i]
#     new_recipe1 <- if (recipe_sum >= 10) (recipe_sum %/% 10) %% 10
#     new_recipe2 <- recipe_sum %% 10

#     recipes <- c(recipes, new_recipe1, new_recipe2)
    
#     loc <- str_locate(
#       str_c(recipes, collapse = ""),
#       score
#     )[,1] - 1
#     if (!is.na(loc)) return(loc)

#     elf1_i <- elf1_i + recipes[elf1_i] + 1
#     while (elf1_i > length(recipes)) elf1_i <- elf1_i - length(recipes)
#     elf2_i <- elf2_i + recipes[elf2_i] + 1
#     while (elf2_i > length(recipes)) elf2_i <- elf2_i - length(recipes)
#   }
# }

Rcpp::cppFunction('
int64_t n_recipes_cpp(std::string score_s) {
  std::vector<int> score;
  std::copy(score_s.begin(), score_s.end(), std::back_inserter(score));
  std::transform(score.begin(), score.end(), score.begin(), [&](int& value){ return value - \'0\'; });

  std::vector<int> recipes = {3, 7};
  int64_t elf1_i = 0;
  int64_t elf2_i = 1;
  int score_i = 0;

  int64_t result = -1;

  auto add_recipe = [&](int new_recipe) {
    recipes.push_back(new_recipe);
    if (score_i >= score.size()) return;

    if (new_recipe == score[score_i]) {
      ++score_i;
    }
    else {
      score_i = 0;
      for (int i = std::max<int>(recipes.size() - score.size(), 0); i < recipes.size(); ++i) {
        for (int j = 0; i + j < recipes.size(); ++j) {
          if (recipes[i + j] != score[j]) break;
          if (i + j == recipes.size() - 1) {
            score_i = j + 1;
            goto done;
          }
        }
      }
done:
    ;
    }

    if (score_i >= score.size()) {
      result = recipes.size() - score.size();
    }
  };

  while (result == -1) {
    int recipe_sum = recipes[elf1_i] + recipes[elf2_i];
    
    if (recipe_sum >= 10) {
      add_recipe((recipe_sum / 10) % 10);
    }
    add_recipe(recipe_sum % 10);

    elf1_i = (elf1_i + recipes[elf1_i] + 1) % recipes.size();
    elf2_i = (elf2_i + recipes[elf2_i] + 1) % recipes.size();
  }

  return result;
}
')

answer <- n_recipes_cpp(as.character(input))
answer
