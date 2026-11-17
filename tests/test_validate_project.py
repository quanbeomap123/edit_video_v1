import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import wave

SCRIPT = Path(__file__).resolve().parents[1] / 'capcutedit-v1/scripts/validate_project.py'
SPEC = importlib.util.spec_from_file_location('validator', SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ProjectValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='capcutedit-test-')
        self.root = Path(self.temp.name).resolve()
        self.addCleanup(self.cleanup_fixture)
        (self.root / 'Resources').mkdir()
        (self.root / 'Timelines/t1').mkdir(parents=True)
        with wave.open(str(self.root / 'Resources/voice.wav'), 'wb') as audio:
            audio.setnchannels(1)
            audio.setsampwidth(2)
            audio.setframerate(48000)
            audio.writeframes(bytes(960))
        self.doc = {'id': 't1', 'materials': {'audios': [
            {'id': 'a1', 'path': '##_draftpath_placeholder_example_##/Resources/voice.wav'}],
            'videos': []}, 'tracks': [{'type': 'audio', 'segments': [
                {'material_id': 'a1', 'target_timerange': {'start': 0, 'duration': 10000}}]}]}
        self.put('Timelines/project.json', {'main_timeline_id': 't1', 'timelines': [{'id': 't1'}]})
        for path in ['draft_content.json', 'template-2.tmp',
                     'Timelines/t1/draft_content.json', 'Timelines/t1/template-2.tmp']:
            self.put(path, self.doc)
        self.bin_path('Resources/voice.wav')

    def cleanup_fixture(self):
        temporary_root = Path(tempfile.gettempdir()).resolve()
        if not self.root.is_relative_to(temporary_root) or not self.root.name.startswith('capcutedit-test-'):
            raise RuntimeError('Refusing cleanup outside the test temp directory')
        self.temp.cleanup()

    def put(self, path, content):
        (self.root / path).write_text(json.dumps(content), encoding='utf-8')

    def bin_path(self, path):
        self.put('draft_meta_info.json', {'draft_materials': [
            {'type': 0, 'value': [{'file_Path': './' + path}]}]})

    def errors(self):
        return {entry['code'] for entry in VALIDATOR.validate(self.root)['errors']}

    def test_placeholder_and_relative_paths_pass_without_mutation(self):
        def snapshot():
            return {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in self.root.rglob('*') if p.is_file()}
        before = snapshot()
        self.assertTrue(VALIDATOR.validate(self.root)['ok'])
        self.assertEqual(before, snapshot())

    def test_missing_imported_file_fails_even_when_timeline_media_exists(self):
        self.bin_path('Resources/missing.wav')
        result = VALIDATOR.validate(self.root)
        self.assertFalse(result['ok'])
        self.assertTrue(any(e['code'] == 'missing_media' and
                            'draft_meta_info.json' in e['context'] for e in result['errors']))

    def test_missing_material_id_and_root_mismatch_fail(self):
        self.doc['tracks'][0]['segments'][0]['material_id'] = 'absent'
        self.put('Timelines/t1/draft_content.json', self.doc)
        self.assertTrue({'unresolved_material_id', 'root_active_mismatch'} <= self.errors())

    def test_unreadable_metadata_is_reported(self):
        (self.root / 'draft_meta_info.json').write_text('not json', encoding='utf-8')
        self.assertIn('unreadable_json', self.errors())


if __name__ == '__main__':
    unittest.main()
