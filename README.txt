

		*****	Core MVP Features	*****

Integration with Kanji API:

------
Utilize a kanji database to fetch kanji data, including definitions, readings, and example usage.

-----
Support JLPT-level categorization for kanji lists.

-----
CRUD Functionality for Kanji Database:
Create, Read, Update, and Delete kanji entries in a database to track learning progress.
Store metadata such as date learned, review schedule, and proficiency status.

-----
JLPT-Level Categorization:

-----
Organize kanji based on JLPT levels (N5-N1) to structure study sessions and progression.
Context Sentence Examples:

-----
Provide example sentences for each kanji, with difficulty aligned to JLPT levels.
Fetch sentences via API or pre-built datasets.
Flashcards:

------
Create a flashcard system for studying kanji.
Include the kanji, readings, meanings, and context sentence on each card.
Implement a spaced repetition algorithm to reinforce memory.
Daily Learning and Review Schedule:

-----
Users can learn a set number of new kanji per day (x kanji).
Daily practice includes:
Learning x new kanji.
Reviewing x kanji from the previous day.
Reviewing x kanji from two days prior.
Total kanji reviewed daily equals 3x (new + yesterday + day before).


			***************************************


		*****	Stretch Goals	*****

-----
Kanji Progress Tracker:

-----
Visualize user progress with charts (e.g., kanji learned per week/month).
Display milestones and achievements to motivate learning.
Pronunciation Practice:

-----
Integrate text-to-speech (TTS) for practicing the pronunciation of kanji and example sentences.

-----
Provide a quiz mode for testing pronunciation.
Quiz Modes:

-----
Include multiple-choice questions, typing quizzes, and kanji-to-meaning matching games.
Toggle Hiragana (Furigana):

-----
Allow users to toggle the display of hiragana (furigana) above kanji on the fly via a keypress.

-----
AI-Generated Paragraphs or Stories:

-----
Use an AI LLM API to craft paragraphs or short stories incorporating kanji marked as known by the user.
Stories will dynamically adapt to the user's learning level and known kanji.


			***************************************


		*****	Technical Specifications	*****


===Frontend===

-----
Make a TUI

===Backend===

-----
Database: SQLite for storing kanji data, learning progress, and review schedules.

-----
Kanji API: Utilize kanjiapi.dev for fetching kanji data.
Core Algorithms:

-----
Spaced repetition for flashcards.

-----
Dynamic scheduling of daily kanji (new, one-day-old, two-day-old).
User Interface:

===Home screen===

-----
Daily kanji review schedule.

-----
Links to learn, review, and quiz modes.

-----
Flashcard view:
Flip for meaning and context sentence.

-----! ! ! ! (more important)
Furigana toggle (stretch goal).

-----
AI-generated stories section (stretch goal).


===Testing===

-----
Unit tests for CRUD functionality.

-----
Integration tests for API connectivity and database operations.

-----


			***************************************


		*****	Development Milestones	*****


===Phase 1: Core MVP Development===

-----
Set up kanji API integration.

-----
Build CRUD database.

-----
Implement daily learning and review schedule.

-----
Design flashcard system.



===Phase 2: Context Sentence Integration===

-----
Fetch and display JLPT-aligned context sentences.


===Phase 3: Stretch Goals===

-----
Add progress tracking, pronunciation practice, and quiz modes.

-----
Implement furigana toggle.

-----
Integrate AI API for generating stories.
