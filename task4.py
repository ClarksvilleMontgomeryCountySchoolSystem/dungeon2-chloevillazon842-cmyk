good = r"""
          )
         (.)
         .|.
         l7J
         | |
     _.--| |--._
  .-';  ;`-'& ; `&.
 & &  ;  &   ; ;   \
 \      ;    &   &_/
  F"""---...---"""J
  | | | | | | | | |
  J | | | | | | | F
   `---.|.|.|.---'
               Krogg"""
bad = r"""
                       `;.`;'.  
                     `;);.(~;(`; 
                   `(;);;;;;);(::` 
                    ;)(; ; ;;~;;;(; 
                 `(`;;~-  -~(;~;)`) 
                  ;(`;)    ' ;);;; ;
               `;);;(;`\ ^_/(;)~;;); 
                 (;);.;)   ':);( ..(;  
                  `'((;);   )(.');`: 
                   ;.' );("'(""/; ;`.)
                    |  | / / \ \;);:
                    |  |/ /WwW\ \;`'
                     \   /) .X.\  \
                      \_/   .X. \_/ TS """

drawbridge_raised = True

if not drawbridge_raised:
    outcome = "Thunder: Lets go. We can leave."
    print(good)
else:
    outcome = "Doom: That sucks. What now?"
    print(bad)
print(outcome)