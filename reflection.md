# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game looked like it was a normal functioning game. Beofre I played the game it described everything clearly and visually did not look like it had any errors.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - New Game button does not work - The game does not restart the number of attmpets a user has when clicking on a different diffucltiy levels.
  - The score does not reset
  - attempting to switch levels does not restart the amountof quesses or the secret number.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input           | Expected Behavior | Actual Behavior                                     | Console Output / Error  |
| --------------- | ----------------- | --------------------------------------------------- | ----------------------- |
| new game button | Start a new game  | only resets the secret and does not reset the score | No console output/Error |
| Submit Guess    | An accurate hint  | The hint is incorrect                               | overflow error          |
| Score reset     | Reset score       | score does not reset/increase when changing levels  | No console output/Error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  The AI tools used was AI and a Claude.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When attepmting the promt from the example "Move the check_guess function to logic_utils.py, update the logic to fix the high/low bug, and update the import in app.py." This lead to the check_guess fuctnion to be moved to the logic_utils.py, but the try block was removed. Follwoing this and testing the game again, it shows a "TypeError: '>' not supported between instances of 'int' and 'str'".

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI did suggest to remove the str() conversion from the "if submit" statement. This allowed the TypeError to disappear as well as suggesting to change the output statment to ensure that they produce the correct statmetn if a number is low or higher.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  To verify if a bug was really fixed I mannualy inputed some numbers to see if the issue was resolved.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Using a generated pytest I was able to test of both bugs were fixed. For example, an example the secret number was 50, and the guess was 60. This tested if the program correctly identified if the number was high. The result was what was predicated.

- Did AI help you design or understand any tests? How?
  AI did help me understand the test because prioe to this I was unsure on how to make a test file in python. Looking though the file it is easy to understand what is happening due to the comments provided.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns execute the entire scripts all over again when someone interacts with the app.
  Session states are built in memory that stores and keeps values available across the reruns, this allows the app to maintain its state rather than resetting it everytime.

  For example if a teacher earaases and rewrites a whiteboard eberytime someone asks a question. This would be like streamit resruns. To keep and not lose all the important information, after the baord has been earsed, you would keep a notebook. This would be like session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    For future use, I would have to reuse is checking the console log to see how each input affects it.

- What is one thing you would do differently next time you work with AI on a coding task?
  I would try to make a more specific prompt and ask for more clarifications.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI generated code can be a great way to prototype but while AI can generate code, that does not mean it is bug free and it is necessary to test and improve the code.
