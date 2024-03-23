import streamlit as st

def write_content(text):
    st.write(text)

def add_title(text):
    st.title(text)

def add_header(text):
    st.header(text)

def add_subheader(text):
    st.subheader(text)

def add_markdown(text):
    st.markdown(text)


add_title('Coding stories about people living with HIV/AIDS')
write_content('Analyze 6 Personal stories (short) from people living with HIV')
add_markdown('**Research question**: understanding experiences and the perceptions of HIV-positive people')
add_markdown("[Text data]: https://pozhet.org.au/living-with-hiv/personal-stories/")

add_markdown('***Coding ledgends***')
add_markdown(''':orange[symptoms]  
:violet[disclosure]  
:red[initial feeling(lost/insecure or fine)]  
:gray[confident/be positive]  
:blue[social insecurity]  
:green[family reaction]  
help from society  
:rainbow[final attitude]''')

add_subheader('Story of Colin')
add_markdown(''':orange[he had recently been sick to the point of having a temperature of over 41 degrees]  
:violet[ his blood donation had shown he was HIV-positive.]  
:red["My first thoughts after that call were, 'I'm finished I'm dead," Colin says]  
:gray[Colin rode with the bumps and decided to wear his HIV on his sleeve.]  
:blue[But you can never know how someone will react when you tell them that you are HIV+. , “There's a lot of misinformation out there and even while I was going through my treatment, teachers were teaching my kids the wrong 'facts'.]  
:green[My youngest was 14 at the time and I came up with some myth-busting style questions, like: did you know I'm not going to die from HIV? He started crying because, from what he had learned, he thought I was.”]  
those facing a possible diagnosis needed to talk to someone 'who knew' that being HIV-positive was not the “be all and end all.”  
:rainbow[As for advice for someone newly diagnosed, he offers this: “It's not the end of the world.]''')

add_subheader('Story of Dianne')
add_markdown(''':orange[compromised immune system and toxoplasmosis on the brain.]  
:violet[ “While I was in hospital, I started to understand that the doctors were recognising each of these conditions as AIDS-defining illnesses,” she recalls.]  
:red[. I took a big breath in and breathed out a sigh of relief and said, 'Thank god for that!’”]  
:gray[“All I could think was you have just given me a life sentence, when I've been living the last week with a death sentence,” she explains.]   
:green[She chose to tell each of her children and had to manage not only their emotions, but who they might speak with about it, and her youngest had to be tested himself. , “My partner, who I had been with for years since separating from my ex-husband, was my rock  Without his love and support, I'm not sure I would have coped,” she says.]  
:rainbow[“I think when you get that diagnosis, you go into a state of grief and shock. You must be gentle on yourself ]''')

add_subheader('Story of Sanaa')
add_markdown(''':orange[ Sanaa begun forming hard, ball-shaped lumps in her underarms. ]  
:violet[ so I was very shocked when the result came back positive for HIV,” she says.]  
:red[“At the time, I was living alone in an isolated, regional community and my family  my community  were so far away in my homeland.”]  
:gray[“HIV has taught me to be more open, to be less judgemental and the importance of building my own resilience.]  
:blue[I would think about it every night. Then, there was and is still a disclosure issue due to my African background.”, “Disclosure in my community is not an individualistic action. Because we have such a strong communal approach to how we live, you must consider the impact your disclosure will have on your community. ]  
:green[“The first person I told was my eldest daughter. A week after I told her, she phoned me and explained she had been quiet because she was trying to get used to the idea and that she had since thought about it, and decided she wouldn't judge me and that she would support me with anything I needed.”]  
her doctor connected her with a social worker, and he encouraged her to find comfort in others experiencing what she was.  
:rainbow[She says: “No matter how bad a situation has been, each one of us has a positive story to tell and it's this positivity that keeps each of us going, and that lives on for others needing something to hold up as hope. For me, talking about it is therapy.”]''')

add_subheader('Story of Peter')
add_markdown(''':violet[my blood test had come back and I was HIV positive.]  
:red[At the time all I knew about HIV was that if you got it you were going to die.]  
:gray[ My CD4 and viral load improved but to me it didn't matter because I still had HIV and no friends.]  
:blue[ As I sat there I could see her lips moving but I couldn't hear her voice because the voice in my head blocked hers out. All I could think about was what I was going to do and what were people going to say.]  
:green[ I knew the chances I was taking drugs and using needles and now I was being punished so don't come crying to her. So my fear of rejection had started, my family didn’t want to know me which I had expected but I thought if you had news like I had my mother would understand and support me.]  
I moved back to Sydney with the help of BGF which I'm very grateful to.
The second service I hooked up with was Pozhet  
:rainbow[So to end on a pleasant note if you are reading and have just been told that you are positive, life doesn't stop because we're positive. There are people in the world that really care and life is worth “Living” but you need support and friends.]''')

add_subheader('Story of Bill')
add_markdown(''':orange[In late 2012 I suddenly became ill with a fever and body rash.]  
:violet[In the December a blood test confirmed I had HIV.]  
:red[This was a shock to me as being heterosexual and not engaging in the more “risky” activities HIV was the last diagnosis I had expected.]  
:blue[Initially I withdrew from my social cycle. After all how could I explain constant sweats and a body rash? It didn't look good. I spent Christmas 2012 day alone with my little dog.]  
In January 2013 the Albion Centre put me in contact with Pozhet.  
:rainbow[At Pozhet I saw people beginning to believe that having HIV doesn't make them dirty or low-class any more than having diabetes or a heart condition does. People who often for the first time in years began to see hope in their lives. Pozhet….I salute you!!]''')

add_subheader('Story of Susie')
add_markdown(''':violet[ I contracted HIV 17 years ago, diagnosed 9 years ago]  
:red[30 years of age and terrified to die and leave my children behind.]  
I also attend the retreats Pozhet hold. This helps me to keep great mental health, socialise, and discuss HIV with friends.''')

st.image('HIV_stories.jpg')