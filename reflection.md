# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

-- The game looked normal when I started until I started playing around the dropdowns and buttons.
-- The concrete bugs I noticed at the start were:
  1. The difficulty 'Range' and 'Attempts allowed' were not matching with the Difficulty setting being selected. For example: Difficulty 'Normal' had range from 1 to 100 whereas 'Hard' had range from 1 to 50 which seems counterintuitive. Attempts allowed was also '5' for 'Hard' and '6' for 'Easy'.
  2. The hints also seems to be opposite. For example: When it was supposed to be 'lower' it shows 'Go HIGHER!' and vice-versa.
  3. I also noticed that when the game was over and I tried to start a new game with 'New Game' button, it did reset and start a new game but, I wasn't able to submit the answer with 'Submit Guess' button.
  4. Another bug I observed was that the 'Secret' number that was being generated based on the 'Difficulty' range was not accurate.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

-- I used Copilot(GPT-5.3-Codex) for this project as instructed.
-- 


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
