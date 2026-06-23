# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      The purpose of the game is to allow users to guess a number between a certain range depending on the difficulty level.
- [ ] Detail which bugs you found.
      I found that the New Game button was not functioning correct and that the number of attempts and history was not being recorded correctly.
- [ ] Explain what fixes you applied.
      Fixes where that applied were moving the location of where the Developer Bug Infor was placed, and where the check_guess fucntion was located, alonf with removing the line that had the number converted to str().

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 5
2. Game returns "Go Lower"
3. User enters a guess of 1
4. The game continues, updating the score and history
5. the Game ends after the correct guess - 4

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
collected 7 items

tests/test_game_logic.py::test_winning_guess_returns_win PASSED                                                        [ 14%]
tests/test_game_logic.py::test_guess_above_secret_is_too_high PASSED                                                   [ 28%]
tests/test_game_logic.py::test_guess_below_secret_is_too_low PASSED                                                    [ 42%]
tests/test_game_logic.py::test_too_high_hint_points_lower PASSED                                                       [ 57%]
tests/test_game_logic.py::test_too_low_hint_points_higher PASSED                                                       [ 71%]
tests/test_game_logic.py::test_int_comparison_does_not_raise PASSED                                                    [ 85%]
tests/test_game_logic.py::test_boundary_one_above_and_below PASSED                                                     [100%]

===================================================== 7 passed in 0.09s =====================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
