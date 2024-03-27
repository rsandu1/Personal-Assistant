import openai
import tkinter as tk

openai.api_key = "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"

def setup(root: tk.Tk) -> None:
    def keyup(event: tk.Event):
        if event.keysym != 'Return':
            return

        nonlocal text
        messages = []
        line = text.get('end -2 lines', 'end').strip().lower()
        if line in ["bye", "quit"]:
            root.quit()
        messages.append({"role": "user", "content": line})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        text.insert('end', reply + '\n', 'response')


    text = tk.Text(root)
    text.pack(fill=tk.BOTH, expand=True)
    text.tag_configure('response', foreground='cyan')
    text.bind('<KeyRelease>', keyup)
    

def main() -> None:
    root = tk.Tk()
    root.title('Personal Assistant: Ask Me Anything!')
    setup(root)
    root.mainloop()


if __name__ == '__main__':
    main()