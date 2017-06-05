import boto3
session = boto3.Session(profile_name='default')
polly_service = boto3.client('polly')
r_voices = polly_service.describe_voices(
    LanguageCode='en-GB'
)
for voice in r_voices['Voices']:
   print(voice) 
   print(voice['Id'])

my_text = 'Hello, Renjith'
polly_response = polly_service.synthesize_speech(
    OutputFormat='mp3',
    Text=my_text,
    TextType='text',
    VoiceId='Emma' # English - British female voice
)

synthesizer = VoiceSynthesizer(0.1)
synthesizer.say("Attention blue zone is for loading and unloading only.")




