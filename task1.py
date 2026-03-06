good = r"""" -=[ Bible ]=-  3/97
                  ,   ,
                 /////|
                ///// |
               /////  |
              |~~~| | |
              |===| |/|
              | B |/| |
              | I | | |
              | B | | |
              | L |  /
              | E | /
              |===|/
         jgs  '---'"""
bad = r"""
              Bullying, in 'da playground:

                         ///.
                        //  7
                        Y `-__.`. .\\
                        /  .----' 7'/
                       /   /    \\/  \
                      /___/      | a=' 
                      \  \      /_ /  
                      /  /      \\ \  
                     / .'        \\ \ 
                     `--`        ''-' AsH

"""

torch_lit = True
if torch_lit:
    outcome = "Flicker: Please put it out your scaring me"
    print(good)
else:
    outcome = "Doom: Please light it again I want it"
    print(bad)
print(outcome)