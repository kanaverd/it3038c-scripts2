This is a strong password generator using Python and the 'random' module. 

I created this since I must change my admin password monthly at work and I dislike coming up with new passwords on my own.
I can use this script to randomly generate a strong 21 character length password without the use of external tools
which I suppose is slightly safer than using other password generators.

Once the Python script is ran, it will ask you what length you want the password to be. Once you press enter with the 
desired length, it will print out the randomly generated password. The only way I have found to break this script is
by entering a number that is bigger than the actual character pool it uses to make the password. I think this feature is
important since my admin password requires 21+ characters but most other passwords only require 8+ so you can decide how
much you want to balance convenience and security for some passwords. 