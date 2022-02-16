# English to Pig Latin Translator
Translate English into Pig Latin!

Read `pig_latin_rules.pdf` for a basic rundown of the rules that were followed in making this Pig Lating translator. The only rule that was not followed was the **Compound Word Rule** because it is far too complex for this simple project to implement.

If you want to challenge yourself or use this as an exercise, do not look at `solution.py`! If you find any issues or have any suggestions for improvements to the solution or the tests, you may submit a pull request! If you're just here for the translation code, `solution.py` is what you want.
## Testing & Developing your own translator
The tests in `test_translate_word.py` & `test_translate.py`
are meant to help you as you develop your translator and to validate your
translator to make sure it correctly translates English in to Pig Latin.

Start by running the tests in `test_translate_word.py`.
Once all the tests in that file pass, then also start testing
your translator against the tests in `test_translate.py`.

Running the tests is very simple. In a terminal, change your directory to where you cloned this repo and type:
```python
# Run all single word tests
python3 test_translate_word.py
```
There are a lot of tests, and they will all run when running the above code.
Feel free to comment out tests that you don't want to run
or alternatively, you can run tests individually by specifying the class
name followed by the test name like so:
```python
# Run a specific test
python3 test_translate_word.py TestTranslateWord.test_consonant_rule_titlecase
```

## Example - Translating Psalm 47
Below is Psalm 47 and its pig latin translation using `solution.py`

You can run this test yourself like so:

```python
python3 test_translate.py TestTranslate.test_translate_psalm47
```

![pig_latin](https://user-images.githubusercontent.com/5977736/154172842-e87c0592-b410-4549-9d8d-e44468addb88.png)