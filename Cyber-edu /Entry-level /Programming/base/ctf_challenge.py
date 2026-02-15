from pwn import *

# Connect to the server
io = remote('34.40.37.6', 30278)

# Loop this if the server sends multiple questions in one connection
while True:
    try:
        # Read the question
        question = io.recvline().decode()
        print(f"Received: {question}")
        # Check for the flag (if the server sends it after the answer)
        if "flag" in question.lower() or "CTF{" in question:
            print(f"FOUND FLAG: {question}")
            break

        # Extract the content between << and >>
        if '<<' in question:
            check = question.split('<<')[1].split('>>')[0]
            print(len(check))
            # Question Type 1: Small number (likely math/integer)
            if len(check) == 8:
                answer = int(check) # Convert to string to send
                print(f"Sending Int Answer: {answer}")
                io.sendline(hex(answer))

            # Question Type 2: Long hex string (ASCII conversion)
            elif len(check) == 40:
                answer = bytes.fromhex(check).decode('ascii')
                print(f"Sending ASCII Answer: {answer}")
                io.sendline(answer.encode()) # Send the decoded word
            elif len(check) == 99:
                octal_array = check.split(' ')
                octal_array_to_ascii = [chr(int(i, 8)) for i in octal_array]
                answer = ''.join(octal_array_to_ascii)
                io.sendline(answer)
        
    except EOFError:
        print("Server closed the connection.")
        break

# Switch to manual mode if you need to see the final output
io.interactive()