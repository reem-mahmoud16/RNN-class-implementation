from clients.gemini_client import GeminiClient

def main():
    client = GeminiClient()
    prompt = input("Enter your text: ")
    #print(system_prompt)

    print(client.generate_content((client.system_prompt)%prompt))


if __name__ == "__main__":
    main()