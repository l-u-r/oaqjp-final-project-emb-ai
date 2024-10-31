import unittest
from EmotionDetection.emotion_detection import emotion_detector
 
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        text = "I am glad this happened"
        result_1 = emotion_detector(text)
        self.assertEqual(result_1['dominant_emotion'], "joy")
        text = "I am really mad about this"
        result_2 = emotion_detector(text)
        self.assertEqual(result_2['dominant_emotion'], "anger")
        text = "I feel disgusted just hearing about this"
        result_3 = emotion_detector(text)
        self.assertEqual(result_3['dominant_emotion'], "disgust")
        text = "I am so sad about this"
        result_4 = emotion_detector(text)
        self.assertEqual(result_4['dominant_emotion'], "sadness")
        text = "I am really afraid that this will happen"
        result_5 = emotion_detector(text)
        self.assertEqual(result_5['dominant_emotion'], "fear")

unittest.main()