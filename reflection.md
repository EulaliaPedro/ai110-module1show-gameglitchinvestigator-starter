# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked like it was a normal functioning game. Beofre I played the game it described everything clearly and visually did not look like it had any errors. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  * New Game button does not work - The game does not restart the number of attmpets a user has when clicking on a different diffucltiy levels. 
  * The score does not reset
  * attempting to switch levels does not restart the amountof quesses or the secret number.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input         | Expected Behavior               |                     Actual Behavior               | Console Output / Error |
|---------------|---------------------------------|---------------------------------------------------|------------------------|
|new game button| Start a new game                |only resets the secret and does not reset the score| No console output/Error   
| Submit Guess  | Number of attempts is diiferent | can't enter more attempts when switching levels   | overflow error   
|Score reset    | Reset score                     |score does not reset/increase when changing levels | No console output/Error   

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  The AI tools used was AI and a Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
