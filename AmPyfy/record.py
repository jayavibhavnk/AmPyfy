


def export(history):
    from pydub import AudioSegment
    from pydub.playback import play
    count = 0
    final = AudioSegment.from_file("drums1.wav")
    for cycle in history:
        drum1 = cycle[0][0]
        drum2 = cycle[1][0]
        bass = cycle[2][0]
        mel = cycle[3][0]
        custom = cycle[4][0]
        audio1 = AudioSegment.from_file("drums{}.wav".format(str(int(drum1)+1)))
        audio2 = AudioSegment.from_file("drums{}.wav".format(str(4+int(drum2)+1)))
        audio3 = AudioSegment.from_file("bass{}.wav".format(str(int(bass)+1)))
        audio4 = AudioSegment.from_file("mel{}.wav".format(str(int(mel)+1)))
        audio5 = AudioSegment.from_file("custom{}.wav".format(str(int(custom)+1)))

        mixed = audio1.overlay(audio2)
        for i in [ audio3, audio4, audio5]:
            mixed = mixed.overlay(i)
        if count == 0:
            final = mixed
            count = 1
        else:
            final += mixed
    final.export("audio.wav",format = 'wav')

        
    