import factory
import yaml

def main():
    config = yaml.load(open('config.yaml', 'r'), Loader=yaml.FullLoader)
    print(config)
    c = factory.ChatFactory().build(config["Chat"])
    sr = factory.SrFactory().build(config["Sr"])
    tts = factory.TTSFactory().build(config["TTS"])

    while True:
        print("请说话: ")
        msg = sr.listen()
        # msg = input("请输入要发送的消息: ")
        if not msg:
            continue

        print(f"发送: {msg}")
        reply = c.chat(msg)
        print(f"收到回复: {reply}")
        tts.speak(reply)

if __name__ == '__main__':
    main()
