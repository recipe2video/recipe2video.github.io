#Recipe-to-Video Questions Dataset

JSON: format:
- `title`, `ingredients_list`, `content`: Raw text from the original recipe.
- `steps_offset`: Index of each cooking step's start in `content`.
- `sents_offset`: Index of each sentences' start in `content`.
- `ingredients`, `props`, `verbs`, `events`, `instantiations`: Contain rich annotations of the recipe.
  - `mention`: Name of entity in raw text.
  - `name`: Base form of entity.
- For the `verb` field:
  - `visual_data`
    - `reference`: List containing a YouTube id and timestamp corresponding to a snippet of video representing the specified verb in context.
    - `objects`: Contains key, value pair, where each key is seconds passed since the timestamp in `reference`, and the values are lists of object ids from `object_class_file.csv`.
- `questions`: Collection of question-answer pairs, auto-generated based on the annotated recipe. For a detailed description of the question families included, see https://r2vq.org/.
