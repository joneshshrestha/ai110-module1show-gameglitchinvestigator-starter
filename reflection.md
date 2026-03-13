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
-- The refactoring was correct and it also correctly imported the functions from logic_utils.py and fixed the bugs I mentioned. I verified this by looking at the code and running the final pytest which shows all 13 test cases passed.
-- The incorrect AI suggestion was I got that was incorrect or misleading was when I used Copilot to create a test_game_logic.py file inside test directory. The first issue was it tired to import the logic_utils.py not considering the file was outside the tests directory and can't be imported just by simple `from logic_utils`. And the second issue was it tried to import the function that was not yet refactored from app.py into logic.py. I verified this when I ran the `pytest` command and checked the terminal output as well as the test file. 
The test cases also included result = check_guess(...) then asserted result == "Win" / "Too High" / "Too Low" for (test_winning_guess, test_guess_too_high, test_guess_too_low). Since check_guess returns a (outcome, message) tuple, these comparisons would always be False. Fixed by unpacking the tuple. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

-- I considered a bug fixed only after I applied the change, and then fail to reproduce that same bug. I also checked that the fix did not break other features by testing different difficulty settings and full game.
-- One manual test I ran was: select each difficulty, start a new game, and verify that the range shown in the sidebar matched the actual secret behavior and that hints pointed in the correct direction. This showed me the range mapping and hint logic were now consistent with the selected difficulty. I also ran `pytest` and confirmed all 13 tests passed, which gave me confidence that the core game logic functions were behaving correctly.
-- AI helped me design and understand tests by suggesting test cases for difficulty ranges, hint direction checks, and parse/validation behavior, then I verified and corrected the assertions where needed.

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
