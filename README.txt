LEETHUB TOPIC SORTER

Purpose:
Copies LeetHub Java solutions from the java/ folder into your existing DSA topic folders.

Setup:
1. Extract these three files into the ROOT of your local java-dsa-journey folder.
   The root is the folder containing README.md, java/, Arrays/, LinkedList/, etc.
2. Keep sort_leethub.py and problem_topics.json there.
3. Edit problem_topics.json to add more LeetHub folder slugs and their DSA topics.

Run in Windows PowerShell from the repository root:
    py .\sort_leethub.py

If the py command is unavailable:
    python .\sort_leethub.py

Safety:
- Copies files; does not move or delete LeetHub originals.
- Does not overwrite files already in the destination.
- Only processes .java and .md files inside java/.
- Unknown problem slugs are reported as UNMAPPED. Add them to problem_topics.json.
- Run it after LeetHub syncs a new accepted solution. It is not a background watcher.
