from datetime import datetime, timezone
import unittest
from app.pipeline import DemoTranslator, SessionMemory, clean_source, process_text

GLOSSARY={'은혜':'grace','믿음':'faith'}; TRANSLATOR=DemoTranslator()

class TranslationPipelineTests(unittest.TestCase):
    def test_correction(self): self.assertEqual(clean_source('하나님의 은에',{'은에':'은혜'}),'하나님의 은혜')
    def test_partial_is_suppressed(self):
        segment=process_text('오늘 말씀을',is_final=False,glossary=GLOSSARY,translator=TRANSLATOR)
        self.assertEqual(segment.status,'suppressed'); self.assertEqual(segment.translated_text,'')
    def test_final_translation_and_glossary(self):
        segment=process_text('오늘 말씀을 통해 하나님의 은혜를 기억합니다.',is_final=True,glossary=GLOSSARY,translator=TRANSLATOR,now=datetime(2026,7,23,tzinfo=timezone.utc))
        self.assertEqual(segment.status,'final'); self.assertIn('grace',segment.translated_text); self.assertIn('은혜 → grace',segment.glossary_matches)
    def test_memory_limit_and_final_only(self):
        memory=SessionMemory(max_segments=2)
        for i in range(3): memory.add(process_text(f'완성된 문장 {i}',is_final=True,glossary=GLOSSARY,translator=TRANSLATOR))
        memory.add(process_text('미완성',is_final=False,glossary=GLOSSARY,translator=TRANSLATOR))
        self.assertEqual(len(memory.items()),2); self.assertTrue(all(x['status']=='final' for x in memory.items()))

if __name__=='__main__': unittest.main()
