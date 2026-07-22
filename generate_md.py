# -*- coding: utf-8 -*-
import os

dialogue = [
    ("Lucas", "Hi everyone. I'm Lucas.", "안녕하세요 여러분. 저는 Lucas입니다."),
    ("Sophia", "And I'm Sophia.", "그리고 저는 Sophia입니다."),
    ("Lucas", "Welcome back to the American English Podcast. Today, we are tackling the invisible wall that every English learner eventually hits. You know the feeling. You've studied the grammar, you've memorized the vocabulary, you've even watched the hundred videos on how to make the th or the r sound. You know the rule intellectually, but the second you start talking to a native speaker, your tongue just refuses to cooperate. It's frustrating, isn't it? It's like there's a disconnect between your brain and your mouth. You want to say world, but your tongue says word. You want to say think, but your tongue says sink.",
     "American English Podcast에 오신 것을 환영합니다. 오늘 우리는 모든 영어 학습자가 결국 부딪히게 되는 보이지 않는 벽에 대해 다뤄볼 것입니다. 어떤 느낌인지 아실 겁니다. 문법을 공부했고, 단어를 외웠고, 'th'나 'r' 발음을 하는 방법에 대한 영상을 수백 번이나 보셨을 겁니다. 머리로는 규칙을 알지만, 원어민과 대화를 시작하는 순간 여러분의 혀는 협조하기를 거부합니다. 정말 답답하죠? 마치 뇌와 입 사이에 연결이 끊어진 것과 같습니다. 'world'라고 말하고 싶은데 혀는 'word'라고 말하고, 'think'라고 말하고 싶은데 혀는 'sink'라고 말하죠."),
    ("Sophia", "Today, we are telling you the hard truth. Your brain isn't the problem. Your muscle memory is the problem. In 2026, we have all the information in the world at our fingertips, but information is not the same as transformation. You can't think your way into a new accent. You have to train your way into it. Your tongue has been training in your native language for 20, 30, or 40 years. It has an autopilot mode. Every time you speak English, your native language is fighting to take control of the wheel. It's overriding your new linguistic intentions.",
     "오늘 우리는 여러분께 뼈아픈 진실을 말씀드리려 합니다. 여러분의 뇌가 문제가 아닙니다. 근육 기억(muscle memory)이 문제입니다. 2026년 현재, 우리는 세상의 모든 정보를 손끝에서 얻을 수 있지만, 정보는 변화(transformation)와 같지 않습니다. 생각만으로는 새로운 억양을 얻을 수 없습니다. 훈련을 통해 얻어야 합니다. 여러분의 혀는 20년, 30년, 혹은 40년 동안 모국어에 맞춰 훈련되어 왔습니다. 혀에는 '자동 조종(autopilot)' 모드가 있습니다. 여러분이 영어를 말할 때마다 모국어가 운전대를 잡으려고 싸웁니다. 여러분의 새로운 언어적 의도를 무시(override)해 버리는 것이죠."),
    ("Lucas", "Today, we're moving beyond intellectual study. We're treating speech as physical muscle rehabilitation. We're going to identify why your tongue is acting as a physical barrier to your progress, and more importantly, how to break that barrier. By the end of this episode, you won't just understand the mechanics of the tongue, you will have started the process of remapping your neural muscular system for native level resonance. Sophia, let's talk about this autopilot. Why is it so strong?",
     "오늘 우리는 머리로 하는 공부를 넘어설 것입니다. 우리는 말하기를 물리적인 근육 재활 치료로 다룰 것입니다. 왜 여러분의 혀가 발전을 가로막는 물리적 장벽으로 작용하는지, 그리고 더 중요한 것은 어떻게 그 장벽을 부술 수 있는지 알아볼 것입니다. 이 에피소드가 끝날 때쯤이면 혀의 역학을 이해하는 것을 넘어, 원어민 수준의 공명(resonance)을 위해 신경 근육 시스템을 재설계하는 과정을 시작하게 될 것입니다. Sophia, 이 자동 조종 모드에 대해 이야기해 보죠. 왜 이렇게 강력한 걸까요?"),
    ("Sophia", "Well, think about riding a bike. Once you learn how to do it, you don't have to think, \"Okay, now move my left leg. Now balance my weight to the right.\" Your body just does it. Speech is the most complex motor skill humans have. We move dozens of tiny muscles in milliseconds.",
     "자전거 타기를 생각해 보세요. 한 번 타는 법을 배우고 나면, \"좋아, 이제 왼쪽 다리를 움직이고, 무게 중심을 오른쪽으로 맞춰야지\"라고 생각하지 않죠. 몸이 그냥 알아서 합니다. 말하기는 인간이 가진 가장 복잡한 운동 기술입니다. 우리는 수십 개의 미세한 근육을 1000분의 1초 단위로 움직입니다."),
    ("Lucas", "Right. Your tongue is an incredibly strong muscle. In your native language, it has developed grooves, neural pathways that are very deep and very fast. When you try to speak American English, you're trying to drive your car off the road and through the grass. It's bumpy, it's slow, and your tongue, your car, wants to get back on the paved road of your native language. This is why you feel robotic. You are fighting a physical battle. When you focus too much on the rule, you create tension, and tension is the enemy of fluency. Most learners think they need more practice, but if you practice with the wrong muscle memory, you're just making the wrong habit stronger. You aren't making progress, you're just digging a deeper hole.",
     "맞습니다. 혀는 믿을 수 없을 정도로 강한 근육입니다. 모국어를 사용할 때 혀는 아주 깊고 빠른 신경 경로(neural pathways)라는 홈을 파놓았습니다. 여러분이 미국식 영어를 말하려 할 때, 그것은 마치 포장도로를 벗어나 잔디밭 위로 차를 몰고 가는 것과 같습니다. 울퉁불퉁하고 느리죠. 그리고 여러분의 혀, 즉 여러분의 자동차는 다시 모국어라는 포장도로로 돌아가고 싶어 합니다. 이것이 여러분이 로봇처럼 말한다고 느끼는 이유입니다. 여러분은 물리적인 전투를 벌이고 있는 것입니다. 규칙에 너무 집중하면 긴장이 생기고, 긴장은 유창함의 적입니다. 대부분의 학습자는 연습이 더 필요하다고 생각하지만, 잘못된 근육 기억으로 연습하면 잘못된 습관만 더 강하게 만들 뿐입니다. 발전하는 것이 아니라 무덤을 더 깊게 파고 있는 것이죠."),
    ("Sophia", "We have to shift the frame. From this moment on, don't think of yourself as an English student. Think of yourself as an English athlete. You are in the gym. You are doing physical therapy for your mouth. This is the missing link in fluency. We have to delete the old autopilot and install a new one. And that doesn't happen through reading, it happens through repetitive, high-intensity mechanical isolation.",
     "프레임을 바꿔야 합니다. 지금 이 순간부터 자신을 영어 '학생'이라고 생각하지 마세요. 영어 '운동선수'라고 생각하세요. 여러분은 체육관에 있습니다. 입을 위한 물리 치료를 하고 있는 것입니다. 이것이 유창함을 위한 잃어버린 고리입니다. 우리는 오래된 자동 조종 장치를 삭제하고 새로운 장치를 설치해야 합니다. 그리고 그것은 읽기를 통해서는 일어나지 않습니다. 반복적이고 강도 높은 기계적 고립 훈련을 통해서만 일어납니다."),
    ("Sophia", "Let's get into the anatomy of tension. Lucas, where do you see students holding the most tension in their tongues?",
     "이제 긴장의 해부학에 대해 이야기해 봅시다. Lucas, 학생들이 혀의 어느 부분에 가장 긴장을 많이 하는 것 같나요?"),
    ("Lucas", "It's almost always the back of the tongue. In many languages, like Russian, Arabic, or Vietnamese, the back of the tongue is very active and often held quite high or tight. But in American English, the back of the tongue needs to be able to bunch up for the R or drop down for resonance. If the root of your tongue is tight, it creates a physical ceiling. The sound can't get out. It stays trapped in your throat. This is what we call muffled resonance. Let's do a quick test. I want everyone to try to swallow. Now, notice that feeling in the very back of your throat. That tightness, many learners keep 20% of that tightness all the time when they speak English. That chronic tension leads to vocal fatigue. Have you ever felt like your throat hurts after talking in English for 10 minutes? That's not because English is hard, it's because you are fighting against your own established neural pathways. You are essentially driving with the parking brake on. Your native language placement is pulling your tongue back to its old home while you're trying to push it forward into a new American position.",
     "거의 항상 혀의 뒤쪽입니다. 러시아어, 아랍어, 또는 베트남어 같은 많은 언어에서는 혀 뒤쪽이 매우 활발하게 움직이고 종종 아주 높거나 팽팽하게 고정되어 있습니다. 하지만 미국식 영어에서는 R 발음을 위해 혀 뒤쪽을 둥글게 뭉쳐 올리거나, 공명을 위해 낮출 수 있어야 합니다. 만약 혀뿌리가 굳어 있으면, 물리적인 천장이 만들어집니다. 소리가 밖으로 나가지 못하죠. 목구멍 속에 갇혀 있게 됩니다. 이것을 우리는 '답답한 공명(muffled resonance)'이라고 부릅니다. 간단한 테스트를 해보겠습니다. 모두 침을 한 번 삼켜보세요. 이제 목구멍 맨 뒤쪽에서 느껴지는 감각에 집중해보세요. 그 팽팽한 긴장감, 많은 학습자분들이 영어로 말할 때 항상 그 긴장감의 20%를 유지하고 있습니다. 이러한 만성적인 긴장은 발성 피로(vocal fatigue)로 이어집니다. 영어로 10분 동안 말하고 나면 목이 아픈 느낌을 받아보신 적 있나요? 그것은 영어가 어려워서가 아니라, 여러분 스스로 이미 형성된 신경 경로와 싸우고 있기 때문입니다. 본질적으로 주차 브레이크를 채운 채 운전하는 것과 같습니다. 여러분의 모국어 위치 지정이 혀를 원래 집으로 잡아당기는 동시에 여러분은 혀를 새로운 미국식 위치로 밀어내려 하고 있는 것이죠."),
    ("Sophia", "To fix this, we have to find the neutral position. In American English, the tongue likes to sit low and wide in the mouth with the tip just barely touching the back of your bottom teeth. Let's practice finding that. Open your mouth slightly. Let your tongue go completely limp. Imagine it's a wet piece of seaweed sitting on the floor of the ocean. No tension. No work.",
     "이것을 해결하려면 중립 위치(neutral position)를 찾아야 합니다. 미국식 영어에서 혀는 입안에서 낮고 넓게 위치하며, 혀끝은 아래쪽 앞니 뒷면에 겨우 닿을락 말락 한 것을 좋아합니다. 이 위치를 찾는 연습을 해보겠습니다. 입을 아주 약간 벌려보세요. 혀의 힘을 완전히 빼세요. 바다 밑바닥에 놓인 젖은 미역 조각이라고 상상해보세요. 긴장감도 없고, 아무런 힘도 들어가지 않습니다."),
    ("Lucas", "Pause for 30 seconds of neutral tongue practice. Feel that? That is where your American English journey starts, from zero tension. We can't build a new house on an old shaky foundation. We have to clear the site first.",
     "(중립 혀 연습을 위해 30초간 멈춤) 느껴지시나요? 바로 그곳이 여러분의 미국식 영어 여정이 시작되는 지점입니다. 바로 '긴장감 제로' 상태죠. 우리는 흔들리는 옛 기초 위에 새 집을 지을 수 없습니다. 먼저 터를 깨끗이 닦아야 합니다."),
    ("Lucas", "Now, we move into proprioceptive recalibration. That's a big word that just means knowing where your body parts are in space. Most people don't actually feel their tongue. It's just there. But, to change your accent, you have to become hyper aware of the tip, the blade, the sides, and the root of your tongue. We use slow-motion exaggeration to break the reflexes. Think about a martial artist. When they learn a new kick, they do it in slow motion for weeks. They need to feel every single millimeter of the movement. Let's try this with the L to R transition. This is the boss fight for many learners. We're going to say light and right, but we're going to do it so slowly that it takes 5 seconds per word. Ready?",
     "이제 고유수용감각 재조정(proprioceptive recalibration) 단계로 넘어가겠습니다. 이건 우리 몸의 각 부위가 공간의 어디에 있는지 인지하는 것을 뜻하는 어려운 용어입니다. 대부분의 사람들은 실제로 자신의 혀를 느끼지 못합니다. 그냥 거기에 있을 뿐이죠. 하지만 억양을 바꾸려면 혀끝(tip), 혓날(blade), 혀 양옆(sides), 그리고 혀뿌리(root)를 아주 미세하게 의식해야 합니다. 우리는 반사 신경을 깨기 위해 '느린 동작 과장(slow-motion exaggeration)'을 사용합니다. 무술가를 생각해보세요. 새로운 발차기를 배울 때 그들은 몇 주 동안 느린 동작으로 연습합니다. 동작의 단 1밀리미터까지 전부 느껴야 하기 때문이죠. L에서 R로 넘어가는 전환으로 연습해봅시다. 많은 학습자에게 이것은 '최종 보스전'과 같습니다. 우리는 'light'와 'right'를 말할 것인데, 한 단어에 5초가 걸릴 정도로 아주 천천히 할 것입니다. 준비되셨나요?"),
    ("Sophia", "L I T E Feel the tip of your tongue touch that bump behind your top teeth. Hold it there. Feel the pressure. Now release.",
     "L-I-T-E. 혀끝이 윗니 뒤쪽의 잇몸 둔덕(치조)에 닿는 것을 느껴보세요. 그대로 누르고 계세요. 압력을 느끼세요. 이제 떼세요."),
    ("Lucas", "Now R I G H T Do not let the tip touch anything. Pull the sides of your tongue up against your top back molars. Feel the bunching in the back. Hold that tension. Now release.",
     "이제 R-I-G-H-T. 혀끝이 아무 데도 닿지 않게 하세요. 혀 양옆을 위쪽 뒷 어금니 쪽으로 끌어올리세요. 뒤쪽이 뭉쳐지는 느낌을 느껴보세요. 그 긴장을 유지하세요. 이제 떼세요."),
    ("Sophia", "Let's do that 10 times.",
     "이것을 10번 반복해봅시다."),
    ("Lucas & Sophia", "Hosts lead 10 reps of ultra-slow L to R transitions, providing coaching. Feel the contact point. Sense the air moving around the sides.",
     "(진행자들이 매우 느린 L-R 전환을 10회 이끌며 코칭함) 접촉점을 느껴보세요. 혀 양옆으로 공기가 흐르는 것을 감지해보세요."),
    ("Sophia", "We aren't learning sounds right now. We are building mechanical habits. You are literally growing new neural connections between your brain and those specific muscle fibers in your tongue. This is why it feels exhausting. You are actually physically changing your brain, but this is the only way to ensure that when you're in a real conversation, your tongue doesn't default back to your native language.",
     "우리는 지금 소리를 배우는 것이 아닙니다. 기계적인 습관을 들이고 있는 것입니다. 여러분은 글자 그대로 뇌와 혀의 특정 근육 섬유 사이에 새로운 신경 연결망을 키우고 있는 것입니다. 그래서 몸이 지치는 것입니다. 실제로 뇌를 물리적으로 변화시키고 있으니까요. 하지만 이것이 실제 대화 상황에서 혀가 모국어로 자동 복귀하지 않게 보장하는 유일한 방법입니다."),
    ("Lucas", "All right, it's time to turn up the heat. We're moving into the over articulation method. We're going to stretch and strengthen the muscles you've been neglecting. We're going to do a sequence of rapid-fire phonetic shifts. We want to push your tongue to the point of mechanical failure. Mechanical failure is a good thing. It means you've pushed your vocal range to your current limit. That's where the growth happens.",
     "좋습니다, 이제 강도를 높여볼 시간입니다. 과조음 방법(over articulation method)으로 넘어가겠습니다. 그동안 방치해 두었던 근육들을 스트레칭하고 강화할 것입니다. 속사포 같은 음소 전환 시퀀스를 연습해볼 것입니다. 혀를 기계적인 한계점(mechanical failure)까지 몰아붙이려고 합니다. 기계적 한계에 도달하는 것은 좋은 일입니다. 이는 목소리 범위를 현재의 한계까지 밀어붙였다는 것을 의미하니까요. 그 지점에서 바로 성장이 일어납니다."),
    ("Sophia", "Drill one, the TH to S snap. Think. Sink. Think. Sink. Think. Sink. Repeat 20 times at 100 bpm. Coaching, make that th exaggerated. Stick your tongue out. Think, sink. Don't be shy.",
     "첫 번째 드릴, TH에서 S로의 빠른 전환. Think. Sink. Think. Sink. Think. Sink. 100 bpm 템포로 20회 반복합니다. (코칭: TH 발음을 과장해서 내세요. 혀를 밖으로 내미세요. Think, sink. 부끄러워하지 마세요.)"),
    ("Lucas", "Drill two, the r to w glide. Red, wed. Red, wed. Red, wed. Repeat 20 times. Coaching, feel the difference in the lips versus the tongue. For red, it's all tongue. For wed, it's all lips. Don't let them mix.",
     "두 번째 드릴, R에서 W로의 활음. Red, wed. Red, wed. Red, wed. 20회 반복합니다. (코칭: 입술과 혀의 차이를 느껴보세요. red를 할 때는 온전히 혀를 씁니다. wed를 할 때는 온전히 입술을 씁니다. 두 발음이 섞이지 않게 하세요.)"),
    ("Sophia", "Drill three, the triple cluster burn. Stronger, stronger, stronger. Repeat 15 times. That strong cluster is a nightmare for muscle memory. s t r, front to back. s t r onger. Let's do it fast. Stronger, stronger, stronger, stronger, stronger. Continue for 60 seconds.",
     "세 번째 드릴, 삼중 자음군 태우기. Stronger, stronger, stronger. 15회 반복합니다. 이 'strong' 자음군은 근육 기억에 있어서 악몽과도 같습니다. S-T-R, 앞에서 뒤로 이동하죠. s-t-r-onger. 빠르게 해봅시다. Stronger, stronger, stronger, stronger, stronger. 60초 동안 계속합니다."),
    ("Lucas", "Stopping. How does your tongue feel? If it feels like it just went for a run, you did it right. You are breaking the old autopilot by sheer force of repetition.",
     "멈춤. 혀 느낌이 어떤가요? 방금 달리기를 하고 온 것 같다면 제대로 하신 겁니다. 단순 반복의 힘으로 오래된 자동 조종 모드를 깨부수고 계시는 것입니다."),
    ("Sophia", "Now, we can't just do drills forever. We have to move into rhythm linking. This is where the tongue movements sync up with the music of American English. Native speech isn't a series of isolated words. It's a continuous stream of sound. Your tongue needs to learn how to glide from one position to the next without stopping.",
     "이제 계속 드릴만 할 수는 없습니다. 리듬 연동(rhythm linking)으로 넘어가야 합니다. 이것은 혀의 움직임이 미국식 영어의 음악적 리듬과 조화를 이루는 단계입니다. 원어민의 말은 개별 단어의 나열이 아닙니다. 끊임없이 이어지는 소리의 흐름입니다. 혀는 한 위치에서 다음 위치로 멈추지 않고 미끄러지듯 이동하는 법을 배워야 합니다."),
    ("Lucas", "Let's take a common phrase, \"What are you doing?\" In textbook English, \"What are you doing?\" In American muscle memory, \"What are you doing?\" Notice the d sound in what are. That's a flap t. Your tongue tip just flicks the roof of your mouth. It doesn't stop.",
     "흔히 쓰이는 문장인 \"What are you doing?\"을 예로 들어봅시다. 교과서식 영어로는 \"What are you doing?\"입니다. 하지만 미국식 근육 기억으로는 \"What are you doing?(워러유두잉)\"입니다. 'what are'에서 들리는 D 소리를 주목하세요. 그게 바로 플랩 T(flap t)입니다. 혀끝이 입천장을 살짝 튕기고 지나갈 뿐, 멈추지 않습니다."),
    ("Sophia", "Let's practice the flick. Water, water, water. Repeat 20 times. Now the whole phrase, \"What are you doing? What are you doing? What are you doing?\"",
     "튕기기(flick) 연습을 해봅시다. Water, water, water. 20회 반복합니다. 이제 전체 문장입니다. \"What are you doing? What are you doing? What are you doing?\""),
    ("Lucas", "This is how you maintain these patterns in a high-stakes conversations. You don't focus on the letters, you focus on the rhythm. If the rhythm is right, the tongue will follow the path of least resistance, which is now the American path we've been building.",
     "이것이 실전 대화(high-stakes conversations)에서 이러한 패턴을 유지하는 방법입니다. 글자에 집중하지 말고 리듬에 집중하세요. 리듬이 맞으면, 혀는 가장 저항이 적은 길(path of least resistance)을 따르게 될 것이며, 그 길은 이제 우리가 만들어가고 있는 미국식 경로가 될 것입니다."),
    ("Sophia", "But you have to protect these gains. You need a 30-day maintenance plan. You can't just do this once. Muscle memory takes about 30 days of consistent daily input to become the default mode. Spend 10 minutes every morning on these mechanical drills. Do them in the car. Do them while you're brushing your teeth. Make it a ritual.",
     "하지만 이렇게 얻은 결실을 지켜내야 합니다. 30일 관리 계획(30-day maintenance plan)이 필요합니다. 한두 번 해서는 안 됩니다. 근육 기억이 기본 모드로 정착되려면 약 30일 동안 매일 꾸준한 자극이 필요합니다. 매일 아침 10분 동안 이 기계적인 드릴 연습에 투자하세요. 차 안에서든, 양치질할 때든 하세요. 나만의 의식으로 만드세요."),
    ("Lucas", "My tongue is actually exhausted, Sophia. I think we really pushed the limits today.",
     "제 혀가 정말 지쳤어요, Sophia. 오늘 우리는 한계를 제대로 시험해본 것 같네요."),
    ("Sophia", "That's the sign of a good workout, Lucas. We want to hear from you. What is the one word that always makes your tongue trip? Is it rural? Is it statistics? Leave a comment below and let us know. We will pick the hardest word and do a special mechanical breakdown episode just for you.",
     "그게 운동이 잘 되었다는 신호예요, Lucas. 시청자분들의 이야기를 듣고 싶습니다. 여러분의 혀를 항상 꼬이게 만드는 단어 하나는 무엇인가요? 'rural'인가요? 아니면 'statistics'인가요? 아래에 댓글을 남겨 알려주세요. 가장 어려운 단어를 골라 여러분만을 위한 특별 기계 분석 에피소드를 진행하겠습니다."),
    ("Lucas", "If you're ready to take this to the next level, you have to watch our 20-minute high-intensity shadowing drill. It's the perfect companion to today's episode because it forces you to use these new tongue positions at full native speed.",
     "이것을 다음 단계로 끌어올릴 준비가 되셨다면, 저희의 20분짜리 고강도 섀도잉 훈련(high-intensity shadowing drill)을 꼭 보셔야 합니다. 이 훈련은 오늘 에피소드의 완벽한 짝꿍입니다. 왜냐하면 여러분이 이 새로운 혀의 위치를 실제 원어민 속도로 사용하도록 강제하기 때문입니다."),
    ("Sophia", "And please, if this episode helped you understand why you've been stuck, hit that subscribe button. We are here every week to help you rebuild your English from the muscles up.",
     "그리고 만약 이번 에피소드가 여러분이 왜 그동안 정체되어 있었는지 이해하는 데 도움이 되었다면, 구독 버튼을 눌러주세요. 저희는 매주 여러분이 근육부터 시작해 영어를 재구축하도록 돕기 위해 찾아옵니다."),
    ("Lucas", "You have the power to change your voice. It's not a gift you're born with, it's a habit you build. Stay patient, stay consistent, and trust the process. We believe in you. Keep training, keep moving that tongue, and we will see you in the next episode.",
     "여러분은 자신의 목소리를 바꿀 수 있는 힘이 있습니다. 그것은 태어날 때부터 주어지는 재능이 아니라, 여러분이 만들어가는 습관입니다. 인내심을 갖고, 꾸준히 하며, 과정을 신뢰하세요. 저희는 여러분을 믿습니다. 계속 훈련하시고, 계속 혀를 움직이세요. 다음 에피소드에서 뵙겠습니다."),
    ("Lucas & Sophia", "Bye, everyone. Happy training.", "안녕히 계세요, 여러분. 즐겁게 훈련하세요."),
    ("Sophia", "Bye.", "안녕히 계세요.")
]

vocab_list = [
    ("tackle (동사)", "다루다, 씨름하다 (어려운 문제 상황 등을 해결하기 위해 맞붙는 뉘앙스)"),
    ("intellectually (부사)", "지적으로, 머리로는 (머리로는 이해하지만 몸은 안 따라줄 때 자주 씀)"),
    ("disconnect (명사)", "단절, 연결 끊김"),
    ("at one's fingertips (숙어)", "쉽게 이용할 수 있는, 손끝에 있는 (정보 등을 쉽게 찾아볼 수 있다는 뜻)"),
    ("override (동사)", "무시하다, 기각하다, 우선하다 (기존의 설정이나 명령을 덮어씌운다는 느낌)"),
    ("linguistic intentions", "언어적 의도"),
    ("rehabilitation (명사)", "재활 (물리 치료나 근육 재활 훈련을 의미)"),
    ("resonance (명사)", "공명, 울림 (발성 시 목소리의 울림)"),
    ("neural pathway", "신경 경로 (뇌와 근육 사이의 연결망)"),
    ("chronic tension", "만성적 긴장"),
    ("vocal fatigue", "발성 피로, 목의 피로"),
    ("proprioceptive recalibration", "고유수용감각 재조정 (자신의 신체/근육 위치를 인지하는 감각을 다시 맞추는 전문 용어)"),
    ("exaggeration (명사)", "과장 (발음 훈련 시 과장해서 말할 때 씀)"),
    ("rapid-fire (형용사)", "연발하는, 속사포 같은"),
    ("flap t", "플랩 현상 (미국 영어에서 water, letter 등의 t 발음이 굴러가는 소리로 나는 현상)"),
    ("path of least resistance", "가장 저항이 적은 길, 가장 쉬운 길 (습관적으로 편하게 행동하는 방향)"),
    ("high-stakes (형용사)", "위험 부담이 큰, 중대한 (실수하면 안 되는 중요한 대화나 상황)"),
    ("muffled resonance", "답답한 공명, 묻힌 공명 (소리가 밖으로 나가지 못하고 목구멍 안에 갇히는 현상)"),
    ("limp (형용사/동사)", "힘없이 축 늘어진 (혀의 긴장을 완전히 뺀 상태를 묘사할 때 씀)"),
    ("seaweed (명사)", "해조류, 미역 (limp tongue을 비유하기 위해 사용됨)"),
    ("shaky foundation", "흔들리는 기초 (올바르지 않은 근육 기억 위에 훈련을 쌓는 것을 비유)"),
    ("over articulation", "과조음 (발음을 지나치게 명확하고 크게 하여 입안 근육을 훈련하는 기법)"),
    ("mechanical failure", "기계적 한계 (혀의 근육이 완전히 지쳐서 더 이상 움직이지 않을 때까지 몰아붙이는 것)"),
    ("rhythm linking", "리듬 연동 (개별 단어가 아니라 문장 전체의 멜로디와 박자에 맞추어 발음하는 기법)"),
    ("default back (동사구)", "원래대로 돌아가다, 초기값으로 돌아가다 (익숙한 모국어의 발음 습관으로 회귀하는 현상)")
]

md_lines = []
md_lines.append("# YouTube Shadowing Practice")
md_lines.append("")
md_lines.append("**🔗 원본 유튜브 링크 (Original Link):** [https://www.youtube.com/watch?v=oJhU1IGTdoo&list=PL1OnCndYUckbQjCBlqFLPxn4mM7QgTNaG&index=18](https://www.youtube.com/watch?v=oJhU1IGTdoo&list=PL1OnCndYUckbQjCBlqFLPxn4mM7QgTNaG&index=18)")
md_lines.append("")
md_lines.append("## 1. Dialog Script (영어-한글 교대 스크립트)")
md_lines.append("화자별로 영어 스크립트 원문이 먼저 나오고, 바로 아래에 한글 해석이 이어지도록 구성되어 섀도잉 학습에 편리합니다.")
md_lines.append("")

for idx, (speaker, eng, kor) in enumerate(dialogue, 1):
    md_lines.append(f"### **[{idx}] {speaker}**")
    md_lines.append(f"**EN:** {eng}")
    md_lines.append(f"**KO:** {kor}")
    md_lines.append("")

md_lines.append("---")
md_lines.append("")
md_lines.append("## 2. Key Vocabulary & Expressions")
md_lines.append("이 영상에서 섀도잉 연습과 함께 학습하면 좋은 어휘 및 표현 정리입니다.")
md_lines.append("")

for word, meaning in vocab_list:
    md_lines.append(f"- **{word}** : {meaning}")

md_content = "\n".join(md_lines)

# Target directory
target_dir = "G:/내 드라이브/[언어 공부]/유튜브 채널_Amreican English"
os.makedirs(target_dir, exist_ok=True)

output_path = os.path.join(target_dir, "Shadowing_Practice.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Generated {output_path} with {len(dialogue)} dialogue blocks.")
