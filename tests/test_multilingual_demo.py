import unittest

from app.multilingual_demo import LANGUAGES, clean_text, translate_sample

SENTENCE = "우리는 서로를 사랑해야 합니다."


class MultilingualDemoTests(unittest.TestCase):
    def test_languages_are_available(self):
        self.assertEqual([item["code"] for item in LANGUAGES], ["en", "es"])

    def test_spanish_and_english_examples(self):
        en = translate_sample(SENTENCE, language="en")
        es = translate_sample(SENTENCE, language="es")
        self.assertEqual(en["status"], "ready")
        self.assertIn("love", en["translation"])
        self.assertIn("amarnos", es["translation"])

    def test_partial_suppressed(self):
        self.assertEqual(translate_sample(SENTENCE, language="es", is_final=False)["status"], "suppressed")

    def test_low_confidence_is_only_used_when_supplied(self):
        result = translate_sample(SENTENCE, language="en", confidence=0.45)
        self.assertIn("low_supplied_confidence", result["flags"])

    def test_duplicate_final_suppressed(self):
        result = translate_sample(SENTENCE, language="en", previous_final=SENTENCE)
        self.assertIn("duplicate_final", result["flags"])

    def test_unknown_phrase_never_gets_fabricated_translation(self):
        result = translate_sample("예상되지 않은 새로운 문장입니다.", language="es")
        self.assertEqual(result["status"], "unavailable")
        self.assertEqual(result["translation"], "")

    def test_cleaning_and_correction(self):
        self.assertEqual(clean_text(" 하나님의   은에 "), "하나님의 은혜")

    def test_unsupported_language_rejected(self):
        with self.assertRaises(ValueError):
            translate_sample(SENTENCE, language="fr")

    def test_short_segment_suppressed(self):
        self.assertEqual(translate_sample("가", language="en")["status"], "suppressed")

    def test_bad_confidence_rejected(self):
        with self.assertRaises(ValueError):
            translate_sample(SENTENCE, language="es", confidence=1.5)


if __name__ == "__main__":
    unittest.main()
