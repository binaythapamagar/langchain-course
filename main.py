from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))
    information = """
Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is an industrialist, entrepreneur, and former United States public official who is the chief executive officer and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire (in terms of US dollars) in June 2026; as of November 2026, Forbes estimates his net worth to be $849.7 billion.

Musk was born into the wealthy Musk family in Pretoria, South Africa. He emigrated to Canada in 1989; he has Canadian citizenship as his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California, United States, to pursue business ventures. In 1995, he co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal. Musk also became an American citizen in 2002.

In 2002, Musk founded and became CEO and chief engineer of SpaceX, a space technology company. Musk joined Tesla as an angel investor in 2004 and became its CEO and product architect in 2008. In 2015, Musk co-founded OpenAI to advance artificial intelligence (AI) research, but later left; his growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired Twitter, a social networking service, and made significant changes, including rebranding it as X in 2023. His other businesses include Neuralink, a neurotechnology company that he co-founded in 2016, and the Boring Company, a tunneling company that he founded in 2017. In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if certain milestones are met, such as achieving a market capitalization of $8.5 trillion. Musk became the first US-dollar trillionaire upon the initial public offering of SpaceX in June 2026, though a SpaceX stock collapse brought him under the threshold by the next month.

Musk is a supporter of global far-right politics, figures, and political parties. His political activities, statements and views have made him a polarizing figure. He has been criticized for making unscientific, false, and misleading statements, promoting conspiracy theories, and affirming antisemitic, white nationalist, and transphobic comments. His acquisition of Twitter was controversial because, following his pledge to decrease censorship, there was an increase in hate speech and misinformation on the service. His role in the second Trump administration attracted public backlash, particularly in response to DOGE and its cuts to the US Agency for International Development (USAID).

Musk was the largest donor in the 2024 United States presidential election, in which he supported Republican nominee Donald Trump. After Trump's inauguration in January 2025, Musk was an advisor to President Trump and the de facto head of the Department of Government Efficiency (DOGE). Musk left the Trump administration in May 2025 and returned to managing his companies; shortly thereafter he had a public feud with Trump. Musk also became the largest political donor in American history in 2026, when he supported Republican nominees in the midterm elections.

Early life and education
See also: Musk family
Elon Reeve Musk was born on June 28, 1971, in Pretoria, Transvaal Province (Gauteng Province since 1994) South Africa's administrative capital.[3][4] He is of British and Pennsylvania Dutch ancestry.[5][6] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[7][8][9] Musk therefore holds both South African and Canadian citizenship from birth.[10] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at Timbavati Private Nature Reserve.[11][12][13][14]

His maternal grandfather, Joshua N. Haldeman, who died in a plane crash when Musk was a toddler, was an American-born Canadian chiropractor, aviator and political activist in the technocracy movement[15][16] who moved to South Africa in 1950.[17] Musk has a younger brother, Kimbal, a younger sister, Tosca, and four paternal half-siblings.[18][19][9][20] He was baptized as a child in the Anglican Church of Southern Africa.[21][22] The Musk family was wealthy during his youth.[14] Despite both Musk and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[14] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines".[23][24] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[3]

After his parents divorced in 1979, Musk, aged around 9, chose to live with his father because he had an Encyclopædia Britannica set and a computer.[25][5][11] He later regretted his decision and became estranged from his father.[26] Musk has recounted trips to a wilderness school that he described as a "paramilitary Lord of the Flies" where "bullying was a virtue" and children were encouraged to fight over rations.[27] In one incident, after an altercation with a fellow pupil, Musk was thrown down concrete steps and beaten severely, leading to him being hospitalized for his injuries.[28] He described his father berating him after he was discharged from the hospital.[28] Errol denied berating Musk.[29]

Musk was an enthusiastic reader of books, and had attributed his success in part to having read The Lord of the Rings, the Foundation series, and The Hitchhiker's Guide to the Galaxy.[13][30] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[31] At age twelve, in 1983, Musk sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500 (equivalent to $1,600 in 2025).[32][33]

Education
An ornate school building
Musk graduated from Pretoria Boys High School in Pretoria, South Africa.
Musk attended Waterkloof House Preparatory School, Bryanston High School, and then Pretoria Boys High School, where he graduated.[34] He was a decent but unexceptional student, earning a 61/100 in Afrikaans and a B on his senior math certification.[35] He applied for a Canadian passport through his Canadian-born mother to avoid South Africa's mandatory military service,[36][37] which would have forced him to participate in the apartheid regime's mandatory military service for young white South African men,[3] as well as to ease his path to immigration to the United States.[38] While waiting for his application to be processed, he attended the University of Pretoria for five months.[39]

Musk arrived in Canada in June 1989, connected with a second cousin in Saskatchewan,[40][41] and worked odd jobs, including at a farm and a lumber mill.[42] In 1990, he entered Queen's University in Kingston, Ontario.[43][44] Two years later, he transferred to the University of Pennsylvania, where he studied until 1995.[45] Although Musk has said that he earned his degrees in 1995, the University of Pennsylvania did not award them until 1997 – a Bachelor of Arts in physics and a Bachelor of Science in economics from the university's Wharton School.[46][47][48][49][50] He reportedly hosted large, ticketed house parties to help pay for tuition, and wrote a business plan for an electronic book-scanning service similar to Google Books.[51]

In 1994, Musk held two internships in Silicon Valley: one at energy storage startup Pinnacle Research Institute, which investigated electrolytic supercapacitors for energy storage, and another at Palo Alto–based startup Rocket Science Games.[52][53] In 1995, he was accepted to a graduate program in materials science at Stanford University, but did not enroll.[48][46][54] Musk decided to join the Internet boom of the 1990s, applying for a job at Netscape, to which he reportedly never received a response.[55][36] The Washington Post reported that Musk lacked legal authorization to remain and work in the United States after failing to enroll at Stanford.[54] In response, Musk said he was allowed to work at that time and that his student visa transitioned to an H1-B. According to numerous former business associates and shareholders, Musk said he was on a student visa at the time.[56]

Business career
Main article: Business career of Elon Musk
Zip2
Main article: Zip2
External videos
video icon Musk speaks of his early business experience during a 2014 commencement speech at University of Southern California on YouTube
In 1995, Musk, his brother Kimbal, and Greg Kouri founded Zip2, a web software company, with funding from a group of angel investors.[57] They housed the venture at a small rented office in Palo Alto.[58] Replying to Rolling Stone, Musk denounced the notion that they started their company with funds borrowed from Musk's father Errol Musk,[26] but in a tweet, he recognized that his father contributed 10% of a later funding round.[59] The company developed and marketed an Internet city guide for the newspaper publishing industry, with maps, directions, and yellow pages.[60] To impress investors, Musk built a large plastic structure around a standard computer to create the impression that Zip2 was powered by a small supercomputer.[61] The Musk brothers obtained contracts with The New York Times and the Chicago Tribune,[62] and persuaded the board of directors to abandon plans for a merger with CitySearch.[63] Musk's attempts to become CEO were thwarted by the board.[64] Compaq acquired Zip2 for $307 million in cash in February 1999 (equivalent to $590,000,000 in 2025),[65][66] and Musk received $22 million (equivalent to $43,000,000 in 2025) for his 7-percent share.[67]

X.com and PayPal
Main articles: X.com (bank), PayPal, and PayPal Mafia
In 1999, Musk co-founded X.com, an online financial services and e-mail payment company.[68] The startup was one of the first federally insured online banks, and, in its initial months of operation, over 200,000 customers joined the service.[69] The company's investors regarded Musk as inexperienced and replaced him with Intuit CEO Bill Harris by the end of the year.[70] The following year, X.com merged with online bank Confinity to avoid competition.[58][70][71] Founded by Max Levchin and Peter Thiel,[72] Confinity had its own money-transfer service, PayPal, which was more popular than X.com's service.[73]

Within the merged company, Musk returned as CEO. Musk's preference for Microsoft software over Unix created a rift in the company and caused Thiel to resign.[74] Due to resulting technological issues and lack of a cohesive business model, the board ousted Musk and replaced him with Thiel in 2000.[75][d] Under Thiel, the company focused on the PayPal service and was renamed PayPal in 2001.[77][78] In 2002, PayPal was acquired by eBay for $1.5 billion (equivalent to $2.7×109 in 2025) in stock, of which Musk—the largest shareholder with 11.72% of shares—received $175.8 million (equivalent to $320,000,000 in 2025).[79][80] In 2017, Musk purchased X.com from PayPal for an undisclosed amount, stating that it had sentimental value.[81][82] He later used the domain in his rebrand of Twitter to X.

SpaceX
Main article: SpaceX

Musk explaining Starship capabilities to leaders of North American Aerospace Defense Command, U.S. Northern Command, and Air Force Space Command in 2019
In 2001, Musk became involved with the nonprofit Mars Society and discussed funding plans to place a growth-chamber for plants on Mars.[83] Seeking a way to launch the greenhouse payloads into space, Musk made two unsuccessful trips to Moscow to purchase intercontinental ballistic missiles (ICBMs) from Russian companies NPO Lavochkin and Kosmotras. Musk instead decided to start a company to build affordable rockets.[84] With $100 million of his early fortune,[85] (equivalent to $180,000,000 in 2025) Musk founded SpaceX in May 2002 and became the company's CEO and Chief Engineer.[86][87]

SpaceX attempted its first launch of the Falcon 1 rocket in 2006.[88] Although the rocket failed to reach Earth orbit, it was awarded a Commercial Orbital Transportation Services program contract from NASA, then led by Mike Griffin.[89][90] After two more failed attempts that nearly caused Musk to go bankrupt,[88] SpaceX succeeded in launching the Falcon 1 into orbit in 2008.[91] Later that year, SpaceX received a $1.6 billion NASA contract (equivalent to $2.4×109 in 2025) for Falcon 9-launched Dragon spacecraft flights to the International Space Station (ISS), replacing the Space Shuttle after its 2011 retirement.[92] In 2012, the Dragon vehicle docked with the ISS, a first for a commercial spacecraft.[93]

Working towards its goal of reusable rockets, in 2015 SpaceX successfully landed the first stage of a Falcon 9 on a land platform.[94] Later landings were achieved on autonomous spaceport drone ships, an ocean-based recovery platform.[95] In 2018, SpaceX launched the Falcon Heavy; its inaugural mission carried Musk's personal Tesla Roadster as a dummy payload.[96][97] Since 2019,[98] SpaceX has been developing Starship, a reusable, super heavy-lift launch vehicle intended to replace the Falcon 9 and Falcon Heavy.[99] In 2020, SpaceX launched its first crewed flight, the Demo-2, becoming the first private company to place astronauts into orbit and dock a crewed spacecraft with the ISS.[100] In 2024, NASA awarded SpaceX an $843 million (equivalent to $865,000,000 in 2025) contract to build a spacecraft that NASA will use to deorbit the ISS at the end of its lifespan.[101]

Starlink
Main article: Starlink
See also: Starlink in the Russo-Ukrainian War

50 Starlink satellites shortly before deployment to low Earth orbit, 2019
In 2015, SpaceX began development of the Starlink constellation of low Earth orbit satellites to provide satellite Internet access.[102] After the launch of prototype satellites in 2018, the first large constellation was deployed in May 2019.[103] As of May 2025, over 7,600 Starlink satellites are operational,[104] comprising 65% of all operational Earth satellites.[105] The total cost of the decade-long project to design, build, and deploy the constellation was estimated by SpaceX in 2020 to be $10 billion (equivalent to $1.2×1010 in 2025).[106][e]

During the Russian invasion of Ukraine, Musk provided free Starlink service to Ukraine, permitting Internet access and communication at a yearly cost to SpaceX of $400 million (equivalent to $440,000,000 in 2025).[109][110][111][112][113] However, Musk refused to block Russian state media on Starlink.[114][115] In 2023, Musk denied Ukraine's request to activate Starlink over Crimea to aid an attack against the Russian navy, citing fears of a nuclear response.[116][117][118]

Tesla
Main article: Tesla, Inc.
Musks stands, arms crossed and grinning, before a Tesla Model S
Musk next to a Tesla Model S, 2011
Tesla, Inc., originally Tesla Motors, was incorporated in July 2003 by Martin Eberhard and Marc Tarpenning. Both men played active roles in the company's early development prior to Musk's involvement.[119] Musk led the Series A round of investment in February 2004; he invested $6.35 million (equivalent to $11,000,000 in 2025), became the majority shareholder, and joined Tesla's board of directors as chairman.[120][121] Musk took an active role within the company and oversaw Roadster product design, but was not deeply involved in day-to-day business operations.[122] Following a series of escalating conflicts in 2007 and the 2008 financial crisis, Eberhard was ousted from the firm.[123][page needed][124] Musk assumed leadership of the company as CEO and product architect in 2008.[125] A 2009 lawsuit settlement with Eberhard designated Musk as a Tesla co-founder, along with Tarpenning and two others.[126][127]

Tesla began delivery of the Roadster, an electric sports car, in 2008. It was the first mass production all-electric car to use lithium-ion battery cells.[128] Under Musk, Tesla has since launched several other electric vehicles, including the four-door sedan Model S (2012-2026),[129] the crossover Model X (2015-2026),[130] the mass-market sedan Model 3 (2017),[131] the crossover Model Y (2020),[132] and the pickup truck Cybertruck (2023-2027).[133] The company has also constructed multiple lithium-ion battery and electric vehicle factories, called Gigafactories.[134]

In May 2020, Musk resigned as chairman of the board as part of the settlement of a lawsuit from the SEC over him tweeting that funding had been "secured" for potentially taking Tesla private.[135][136]

Since its initial public offering in 2010,[137] Tesla stock has risen significantly; it became the most valuable carmaker in summer 2020,[138][139] and it entered the S&P 500 later that year.[140][141] In October 2021, it reached a market capitalization of $1 trillion (equivalent to $1.2×1012 in 2025), the sixth company in U.S. history to do so.[142]

SolarCity and Tesla Energy
Main articles: SolarCity and Tesla Energy
Musk provided the initial concept and financial capital for SolarCity, which his cousins Lyndon and Peter Rive founded in 2006.[143] By 2013, SolarCity was the second largest provider of solar power systems in the United States.[144] In 2014, Musk promoted the idea of SolarCity building an advanced production facility in Buffalo, New York, triple the size of the largest solar plant in the United States.[145] Construction of the factory started in 2014 and was completed in 2017. It operated as a joint venture with Panasonic until early 2020.[146][147]

Tesla acquired SolarCity for $2 billion in 2016 (equivalent to $2.7×109 in 2025) and merged it with its battery unit to create Tesla Energy. The deal's announcement resulted in a more than 10% drop in Tesla's stock price; at the time, SolarCity was facing liquidity issues.[148] Multiple shareholder groups filed a lawsuit against Musk and Tesla's directors, stating that the purchase of SolarCity was done solely to benefit Musk and came at the expense of Tesla and its shareholders.[149][150] Tesla directors settled the lawsuit in January 2020, leaving Musk the sole remaining defendant.[151][152] Two years later, the court ruled in Musk's favor.[148]

Neuralink
Main article: Neuralink
Musk standing next to bulky medical equipment on a stage
Musk discussing a Neuralink device during a live demonstration in 2020
In 2016, Musk co-founded Neuralink, a neurotechnology startup, with an investment of $100 million.[153][154] Neuralink aims to integrate the human brain with artificial intelligence (AI) by creating devices that are embedded in the brain.[154][155] In September 2023, the Food and Drug Administration approved Neuralink to initiate six-year human trials.[156] The company's animal trials—which have caused the deaths of some monkeys—have led to claims of animal cruelty.[157]

The Boring Company
Main article: The Boring Company
Musk speaks to a crowd of journalists. Behind him is a lighted tunnel.
Musk during the 2018 inauguration of the Boring test tunnel in Hawthorne, California
In 2017, Musk founded the Boring Company to construct tunnels.[158][159] A tunnel beneath the Las Vegas Convention Center was completed in early 2021.[160] Many other company projects in cities across the United States were announced, but subsequently became inactive or were canceled.[161]

X Corp.
Main articles: Acquisition of Twitter by Elon Musk and Twitter under Elon Musk
Avatar of Elon Musk
Elon Musk 
(@elonmusk)
tweeted:
I made an offer
https://sec.gov/Archives/edgar...
April 14, 2022[162]

In early 2017, Musk expressed interest in buying Twitter and had questioned the platform's commitment to freedom of speech.[163][164][165] By 2022, Musk had reached 9.2% stake in the company,[166] making him the largest shareholder.[167][f] Musk later agreed to a deal that would appoint him to Twitter's board of directors and prohibit him from acquiring more than 14.9% of the company.[169][170] Days later, Musk made a $43 billion offer to buy Twitter.[167][171] By the end of April Musk had successfully concluded his bid for approximately $44 billion.[172] This included approximately $12.5 billion in loans and $21 billion in equity financing.[173][174] Having backtracked on his initial decision,[175] Musk bought the company on October 27, 2022.[176]

Immediately after the acquisition, Musk fired several top Twitter executives including CEO Parag Agrawal;[176][177] Musk became the CEO instead.[178] Under Musk, Twitter instituted monthly subscriptions for a "blue check",[179][180][181] and laid off a significant portion of the company's staff.[182][183] Musk lessened content moderation and hate speech also increased on the platform after his takeover.[184][185][186][187] In late 2022, Musk released internal documents relating to Twitter's moderation of Hunter Biden's laptop controversy in the lead-up to the 2020 presidential election.[188] Musk also promised to step down as CEO after a Twitter poll,[189][190] and five months later, Musk stepped down as CEO and transitioned his role to executive chairman and chief technology officer (CTO).[191]

Despite Musk stepping down as CEO, X continues to struggle with challenges such as viral misinformation,[192] hate speech, and antisemitism controversies.[193][194] Musk has been accused of trying to silence some of his critics such as Twitch streamer Asmongold, who criticized him during one of his streams.[195] Musk has been accused of removing their accounts' blue checkmarks, which hinders visibility and is considered a form of shadow banning,[196][197] or suspending their accounts without justification.[198]

OpenAI and xAI
Main articles: OpenAI and xAI (company)
In December 2015, Musk co-founded OpenAI, a not-for-profit artificial intelligence (AI) research company aiming to develop artificial general intelligence, intended to be safe and beneficial to humanity.[199] Musk pledged $1 billion of funding to the company,[200] but only donated $50 million.[201] In 2018, Musk left the OpenAI board.[202] Since 2018, OpenAI has made significant advances in machine learning.[203] In July 2023, Musk launched the artificial intelligence company xAI, which aims to develop a generative AI program that competes with existing offerings like OpenAI's ChatGPT. Musk obtained funding from investors in SpaceX and Tesla,[204] and xAI hired engineers from Google and OpenAI.[205]

Grok
This section is an excerpt from Grok (chatbot).edit
Grok is a series of generative AI large language models developed by SpaceX Super Intelligence. It was launched in November 2023 by Elon Musk as an initiative based on the large language model (LLM) of the same name. Grok has apps for iOS and Android and is integrated with the X social network and Tesla's Optimus robot where it has chatbot functionality. Grok is named after the verb to grok, created by the American science fiction author Robert A. Heinlein to convey a form of deep, intuitive understanding.

SpaceX Super Intelligence has released several Grok models. Grok-1 was open-sourced in 2024,[206] followed by Grok-2, Grok 3, and Grok 4 model families,[207] with Grok 4.5 released in 2026.[208] Different versions added capabilities including image generation,[209] web search,[210] "Think" mode to simulate reasoning,[211], agentic coding tool called Grok Build,[212] and AI teammates called Grok Bot.[213] Musk admitted in 2026 that Grok was partially distilled from OpenAI's GPT models.[214][215] Starting with Grok 4.5, the models are co-developed with incoming SpaceXSI subsidiary Cursor.[208]

Grok also generates articles for the encyclopedia website Grokipedia, launched in October 2025 by Musk as an alternative to Wikipedia, which he described as "woke" and politically biased.

Political positions
Main articles: Views of Elon Musk and Political activities of Elon Musk
See also: Protests against Elon Musk
‹ The template below (Conservatism US) is being considered for merging with Right-wing populism US. See templates for discussion to help reach a consensus. ›
Part of a series on
Conservatism
in the United States

Schools
Principles
History
Intellectuals
Politicians
Jurists
Commentators
Activists
Literature
Parties
Think tanks
Media
Other organizations
Movements
Related
 Conservatism portal
flag United States portal
vte

This section may be unbalanced toward certain viewpoints. Please help improve it by adding information on neglected viewpoints. Relevant discussion may be found on the talk page. (April 2026)
Avatar of Elon Musk
Elon Musk
(@elonmusk)
tweeted:
My commitment to free speech extends even to not banning the account following my plane, even though that is a direct personal safety risk
November 6, 2022[216]

Musk is an outlier among business leaders who typically avoid partisan political advocacy.[217][218][219] Rejecting the conservative label, Musk has described himself as a political moderate,[220] even as his views have become more right-wing over time.[221] By the mid-2020s, his views have been characterized as libertarian[222] and right-wing[223] or far-right,[224] and after his involvement in European politics, they have received criticism from world leaders such as Emmanuel Macron and Olaf Scholz.[225][226][227][228]

Within the context of American politics, Musk supported Democratic candidates up until 2022, at which point he voted for a Republican for the first time.[229][230] He has stated support for universal basic income,[231] gun rights,[232] freedom of speech,[233] a tax on carbon emissions,[234] and H-1B visas.[235] Musk has expressed concern about issues such as artificial intelligence (AI)[236] and climate change,[237] and has been a critic of wealth tax,[238] short-selling,[239] and government subsidies.[240] An immigrant himself, Musk has been accused of being anti-immigration, and regularly blames immigration policies for illegal immigration.[241] He is also a pronatalist who believes population decline is the biggest threat to civilization,[242] and identifies as a cultural Christian.[243][244] Musk has long been an advocate for space colonization, especially the colonization of Mars. He has repeatedly pushed for humanity colonizing Mars, in order to become an interplanetary species and lower the risks of human extinction.[245]

Musk has promoted conspiracy theories and made controversial statements that have led to accusations of racism, sexism, antisemitism,[246][247] transphobia,[248] disseminating disinformation, and support of white pride.[249][250] While describing himself as a "pro-Semite",[251] his comments regarding George Soros and Jewish communities have been condemned by the Anti-Defamation League and the Biden White House.[252] Musk was criticized during the COVID-19 pandemic for making unfounded epidemiological claims,[253] defying COVID-19 lockdowns restrictions,[254] and supporting the Canada convoy protest against vaccine mandates.[255][256] He has amplified false claims of white genocide in South Africa.[257]

Musk was a registered independent voter when he lived in California.[258] Historically, he has donated to both Democrats and Republicans,[259] many of whom serve in states in which he has a vested interest.[260] Musk supported Democrat Barack Obama in 2008 and 2012,[229] Democrat Hillary Clinton in 2016, and Democrat Joe Biden in 2020.[261] In the 2020 Democratic Party presidential primaries, Musk endorsed candidate Andrew Yang and expressed support for Yang's proposed universal basic income,[262] and endorsed Kanye West's 2020 presidential campaign.[263]

Since 2022, his political contributions have mostly supported Republicans, with his first vote for a Republican going to Mayra Flores in the 2022 Texas's 34th congressional district special election.[264][265] In 2022, Musk gave over $50 million to Citizens for Sanity, a conservative political action committee.[266] In 2023, he supported Republican Ron DeSantis for the 2024 U.S. presidential election, giving $10 million to his campaign,[266] and hosted DeSantis's campaign announcement on a Twitter Spaces event.[267][268][269] From June 2023 to January 2024, Musk hosted a bipartisan set of X Spaces with Republican and Democratic candidates, including Robert F. Kennedy Jr.,[270] Vivek Ramaswamy,[271] and Dean Phillips.[272]

In 2024, he started supporting international far-right political parties, activists, and causes,[273] and has shared far-right misinformation[274][275][276] and numerous conspiracy theories.[277][278]

Avatar of Elon Musk
Elon Musk
(@elonmusk)
tweeted:
I fully endorse President Trump and hope for his rapid recovery
July 13, 2024[279]

By the middle of 2024, Musk had become a vocal and financial supporter of Donald Trump.[280] In July 2024, minutes after Trump survived an assassination attempt while speaking in Butler, Pennsylvania, Musk endorsed him for president, saying: "I fully endorse President Trump and hope for his rapid recovery."[281][282] During the presidential campaign, Musk joined Trump on stage at a campaign rally,[283] and during the campaign promoted conspiracy theories and falsehoods about Democrats, election fraud[284] and immigration, in support of Trump.[285][286] Musk was the largest individual donor of the 2024 election, spending $291 million.[287][288] One PAC funded by Musk created and aired deceptive "false-flag" advertisements appearing to come from progressive organizations in order to misrepresent Kamala Harris's positions.[289][290]

Starting in January 2025, Musk's international political actions and comments came under increasing scrutiny and criticism, especially from the governments and leaders of France, Germany, Norway, Spain and the United Kingdom, particularly due to his position in the U.S. government from January to May 2025,[291] as well as ownership of X.[292][293][294] A February 2025 NBC News analysis found he had boosted far-right political movements to cut immigration and curtail regulation of business in at least 18 countries on six continents since 2023.[295]

In 2025, Musk contributed $19 million to the Wisconsin Supreme Court race, hoping to influence the state's future redistricting efforts and its regulations governing car manufacturers and dealers.[296][297] Musk was the largest individual donor in the 2026 United States elections, spending over $474 million in support of Republican candidates, including $216 million to America PAC, $168 million to the Senate Leadership Fund, $30 million to the Congressional Leadership Fund, $10 million to Lone Star Liberty PAC, $10 million to the Republican Governors Association, and $2 million to the Republican Attorneys General Association.[298][299] Musk became the largest political donor in the history of the United States in the 2026 midterm elections.[300]

Salute at Trump's second inauguration
Main article: Elon Musk salute controversy

Musk giving a gesture at the second inauguration of Donald Trump before saying "My heart goes out to you. It is thanks to you that the future of civilization is assured."[301][302]
During his speech after the second inauguration of Donald Trump, Musk twice made a gesture interpreted by many as a Nazi or a fascist Roman salute.[g] It was widely condemned as an intentional Nazi salute in Germany,[304][305][306] where making such gestures is illegal.[307] The Anti-Defamation League said it was not a Nazi salute,[308] but other Jewish organizations disagreed and condemned the salute.[309][310][311][312] American public opinion was divided on partisan lines as to whether it was a fascist salute.[313] Musk dismissed the accusations of Nazi sympathies, deriding them as "dirty tricks" and a "tired" attack.[314][315] Neo-Nazi and white supremacist groups celebrated it as a Nazi salute.[308][316]

Department of Government Efficiency
Main article: Department of Government Efficiency

Musk wielding a chainsaw at the Conservative Political Action Conference (CPAC) in 2025, imitating a publicity stunt used by Javier Milei symbolic of efficiency, federal mass layoffs and tax cutting
The concept of DOGE emerged in a discussion between Musk and Donald Trump, and in August 2024, Trump committed to giving Musk an advisory role, with Musk accepting the offer.[317] In November and December 2024, Musk suggested that the organization could help to cut the U.S. federal budget, consolidate the number of federal agencies,[318][319] and eliminate the Consumer Financial Protection Bureau,[320][321] and that its final stage would be "deleting itself".[322]

In January 2025, the organization was created by executive order, and Musk was designated a "special government employee".[323][324] Musk led the organization and was an advisor to Trump,[325] although his official role is not clear.[326] In sworn statement during a lawsuit, the director of the White House Office of Administration stated that Musk "is not an employee of the U.S. DOGE Service or U.S. DOGE Service Temporary Organization", "is not the U.S. DOGE Service administrator", and has "no actual or formal authority to make government decisions himself".[327][328] Trump said two days later that he had put Musk in charge of DOGE.[329] A federal judge has ruled that Musk acted as the de facto leader of DOGE.[330]

Musk's role in the second Trump administration, particularly in response to DOGE, has attracted public backlash. He was criticized for his treatment of federal government employees,[331][332][333] including his influence over the mass layoffs of the federal workforce.[334][335][336] He has prioritized secrecy within the organization[337] and has accused others of violating privacy laws.[323] A Senate report alleged that Musk could avoid up to $2 billion in legal liability as a result of DOGE's actions.[338] In May 2025, Bill Gates accused Musk of "killing the world's poorest children" through his cuts to USAID.[339] Modeling by Boston University estimated the cuts resulted in 400,000 children and 200,000 adults deaths by November.[340][341][342] Musk departed on May 28, 2025, when the special government employee's 130 day deadline expired.[343][344][345]

Feud with Donald Trump
Main article: Trump–Musk feud
Avatar of Elon Musk
Elon Musk
(@elonmusk)
tweeted:
Time to drop the really big bomb:
@realDonaldTrump is in the Epstein files. That is the real reason they have not been made public.

Have a nice day, DJT!
June 5, 2025[346]

After leaving office, Musk criticized the Trump administration's Big Beautiful Bill, calling it a "disgusting abomination" due to its provisions increasing the deficit.[347] A feud began between Musk and Trump, with its most notable event being Musk alleging Trump had ties to sex offender Jeffrey Epstein on June 5, 2025.[348][349] On June 11, Musk publicly apologized for the tweets against Trump before deleting them, saying they "went too far".[350]

International relations
Main article: International relations of Elon Musk

Musk with Israeli president Isaac Herzog in November 2023
Musk has been critical of Israel's actions in the Gaza Strip during the Gaza war,[351] praised China's economic and climate goals,[352][353] suggested that Taiwan and China should resolve cross-strait relations,[354][355] and was described as having a close relationship with the Chinese government.[352][353]

In Europe, Musk expressed support for Ukraine in 2022 during the Russian invasion, recommended referendums and peace deals on the annexed Russia-occupied territories,[356][357] and supported the far-right Alternative for Germany political party in 2024.[358]

Regarding British politics, Musk blamed the 2024 UK riots on mass migration and open borders,[359][360] criticized Prime Minister Keir Starmer for what he described as a "two-tier" policing system,[361][362][360] and was subsequently attacked as being responsible for spreading misinformation and amplifying the far-right.[363] Musk has publicly supported far-right activist Tommy Robinson, and initially pledged financial backing to Reform UK ahead of the next general election. In January 2025, he publicly fell out with Reform UK leader Nigel Farage, calling for Farage to be replaced as party leader.[364][365] Musk subsequently shifted his backing towards Restore Britain, the political party launched by Rupert Lowe.[366]

Legal affairs
Main article: Legal affairs of Elon Musk
In July 2018, Musk arranged for SpaceX and the Boring Company employees to build a mini-submarine to assist in the rescue of children trapped in a flooded cavern in Thailand. Despite him drawing attention to it on social media,[367] the mini-submarine was deemed not practical for the rescue mission.[368] A British diver interviewed about the mission, Vern Unsworth, reflected on Musk's actions collectively a "PR stunt". In response, Musk referred to Unsworth as a "pedo" in a tweet.[369] In September, Unsworth filed a defamation suit seeking $190 million in damages.[370][371] Musk apologized and a jury later found Musk was not liable for the claim.[372][373]

In September 2018, Musk was sued by the U.S. Securities and Exchange Commission (SEC) for a tweet stating that funding had been secured for potentially taking Tesla private.[135][h] The securities fraud lawsuit characterized the tweet as false, misleading, and damaging to investors, and sought to bar Musk from being CEO of publicly traded companies.[135][377][378] Two days later, Musk settled with the SEC, without admitting or denying the SEC's allegations. As a result, Musk and Tesla were fined $20 million each, and Musk was forced to step down for three years as Tesla chairman but was able to remain as CEO.[136] Shareholders filed a lawsuit over the tweet,[379] and in February 2023, a jury found Musk and Tesla not liable.[380] Musk has stated in interviews that he does not regret posting the tweet that triggered the SEC investigation.[381][382]

In 2019, Musk stated in a tweet that Tesla would build half a million cars that year.[383] The SEC reacted by asking a court to hold him in contempt for violating the terms of the 2018 settlement agreement. A joint agreement between Musk and the SEC eventually clarified the previous agreement details,[384] including a list of topics about which Musk needed preclearance.[385] In 2020, a judge blocked a lawsuit that claimed a tweet by Musk regarding Tesla stock price ("too high imo") violated the agreement.[386][387] Freedom of Information Act (FOIA)-released records showed that the SEC concluded Musk had subsequently violated the agreement twice by tweeting regarding "Tesla's solar roof production volumes and its stock price".[388]

In October 2023, the SEC sued Musk over his refusal to testify a third time in an investigation into whether he violated federal law by purchasing Twitter stock in 2022.[389][390][391] In February 2024, Judge Laurel Beeler ruled that Musk must testify again.[392] In January 2025, the SEC filed a lawsuit against Musk for securities violations related to his purchase of Twitter.[393]

In January 2024, Delaware judge Kathaleen McCormick ruled in a 2018 lawsuit that Musk's $55 billion pay package from Tesla be rescinded.[394] McCormick called the compensation granted by the company's board "an unfathomable sum" that was unfair to shareholders.[395] The Delaware Supreme Court overturned McCormick's decision in December 2025, restoring Musk's compensation package and awarding $1 in nominal damages.[396] Musk exercised the stock options from his 2018 pay package on June 16, 2026.[397][398]

On March 20, 2026, a jury in San Francisco, California, found Musk liable for misleading investors during his acquisition of Twitter, though they absolved him of some fraud allegations, finding he did not "scheme" to defraud investors.[399][400] Specifically, Musk was found to have misled shareholders in two tweets, but not in a podcast, as the views he expressed in that were deemed by the jury to be an opinion.[399][400] Damages have yet to be calculated, but plaintiffs' lawyers estimated them to be $2.5 billion.[401]

On May 18, 2026, a jury in Oakland, California, decided in favor of OpenAI and its executives, finding that Musk's February 2024 claims that the company violated its founding agreement by prioritizing profits over AI safety[402] were barred by the statute of limitations.[403]

Personal life

Official Royal Society portrait, 2018
Musk became a U.S. citizen in 2002.[45] From the early 2000s until late 2020, Musk resided in California, where both Tesla and SpaceX were founded.[404] He then relocated to Cameron County, Texas,[405][406] saying that California had become "complacent" about its economic success.[404][407][408]

While hosting Saturday Night Live in 2021, Musk stated that he has Asperger syndrome.[409] He was not diagnosed as a child.[410] Musk suffers from back pain and has undergone several spine-related surgeries, including a disc replacement.[411][412] In 2000, he contracted a severe case of malaria while on vacation in South Africa.[413]

Musk has stated he uses doctor-prescribed ketamine for occasional depression and that he doses "a small amount once every other week or something like that";[414] since January 2024, some media outlets have reported that he takes ketamine, marijuana, LSD, ecstasy, mushrooms, cocaine and other drugs. Musk at first refused to comment on his alleged drug use, before responding that he had not tested positive for drugs, and that if drugs somehow improved his productivity, "I would definitely take them!"[415] The New York Times' investigations revealed Musk's overuse of ketamine and numerous other drugs, as well as strained family relationships and concerns from close associates who have become troubled by his public behavior as he became more involved in political activities and government work.[416]

Through his own label Emo G Records, Musk released a rap track, "RIP Harambe", on SoundCloud in March 2019.[417][418][419] The following year, he released an EDM track, "Don't Doubt Ur Vibe", featuring his own lyrics and vocals.[420]

Musk plays video games, which he stated has a "'restoring effect' that helps his 'mental calibration'".[421] Some games he plays include Quake, Diablo IV, Elden Ring, and Polytopia.[422][423] Musk once claimed to be one of the world's top video game players but has since admitted to "account boosting", or cheating by hiring outside services to achieve top player rankings.[424][425][426]

Marriages, relationships and children
Further information: Musk family

Musk and his son X Æ A-Xii with President Donald Trump in the Oval Office in February 2025
Musk has fathered at least 14 children, one of whom died as an infant.[427] The Wall Street Journal reported in 2025 that sources close to Musk suggest that the "true number of Musk's children is much higher than publicly known".[2] He had six children with his first wife, Canadian author Justine Wilson, whom he met while attending Queen's University in Ontario, Canada; they married in 2000.[428] In 2002, their first child, Nevada Alexander Musk, died of sudden infant death syndrome at the age of 10 weeks.[429][430] After his death, the couple used in vitro fertilization (IVF) to continue their family;[430] they had twins in 2004, followed by triplets in 2006.[430] The couple divorced in 2008 and have shared custody of their children.[431][432] The elder twin he had with Wilson came out as a trans woman and, in 2022, officially changed her name to Vivian Jenna Wilson,[433] adopting her mother's surname because she no longer wished to be associated with Musk.[433]

Musk began dating English actress Talulah Riley in 2008.[434] They married two years later at Dornoch Cathedral in Scotland.[435][436] In 2012, the couple divorced, then remarried the following year.[437] After briefly filing for divorce in 2014,[437] Musk finalized a second divorce from Riley in 2016.[438] Musk then dated the American actress Amber Heard for several months in 2017;[439][440] he had reportedly been "pursuing" her since 2012.[441]

In 2018, Musk and Canadian musician Grimes confirmed they were dating.[442] Grimes and Musk have three children, born in 2020, 2021, and 2022.[i] Musk and Grimes originally gave their eldest child the name "X Æ A-12", which would have violated California regulations as it contained characters that are not in the modern English alphabet;[447][448] the names registered on the birth certificate are "X" as a first name, "Æ A-Xii" as a middle name, and "Musk" as a last name.[449][450] They received criticism for choosing a name perceived to be impractical and difficult to pronounce;[451] Musk has said the intended pronunciation is "X Ash A Twelve".[450] Their second child was born via surrogacy.[452] Despite the pregnancy, Musk confirmed reports that the couple were "semi-separated" in September 2021; in an interview with Time in December 2021, he said he was single.[453][454] In October 2023, Grimes sued Musk over parental rights and custody of X Æ A-Xii.[455][456][457] Musk has taken X Æ A-Xii to multiple official events in Washington, D.C., during Trump's second term in office.[458]

Also in July 2022, The Wall Street Journal reported that Musk allegedly had an affair with Nicole Shanahan, the wife of Google co-founder Sergey Brin, in 2021, leading to their divorce the following year.[459] Musk denied the report.[460] Musk also had a relationship with Australian actress Natasha Bassett, who has been described as "an occasional girlfriend".[461] In October 2024, The New York Times reported Musk bought a Texas compound for his children and their mothers,[462] though Musk denied having done so.[463]

Musk also has four children with Shivon Zilis, director of operations and special projects at Neuralink: twins born via IVF in 2021, a child born in 2024 via surrogacy and a child born in 2025.[j] In July 2026 Musk described Zilis as his partner.[470]

On February 14, 2025, Ashley St. Clair, an influencer and author, posted on X claiming to have given birth to Musk's son Romulus five months earlier, which media outlets reckoned as Musk's thirteenth child.[k] On February 22, 2025, it was reported that St Clair had filed for sole custody of her five-month-old son and for Musk to be recognised as the child's father.[474][475] On March 31, 2025, Musk wrote that, while he was unsure if he was the father of St. Clair's child, he had paid St. Clair $2.5 million and would continue paying her $500,000 per year.[l] Later reporting from the Wall Street Journal indicated that $1 million of these payments to St. Clair were structured as a loan.[2]

Involvement with Jeffrey Epstein
See also: List of people named in the Epstein files
In 2014, Musk and Ghislaine Maxwell appeared together in a photograph taken at an Academy Awards after-party, which Musk later described as a "photobomb".[480][481] The January 2026 Epstein files contain emails between Musk and Epstein from 2012 to 2013, after Epstein's first conviction.

Emails released on January 30, 2026, indicated that Epstein invited Musk to visit his private island on multiple occasions.[482] The correspondence showed that while Epstein repeatedly encouraged Musk to attend, Musk did not visit the island. In one instance, Musk discussed the possibility of attending a party with his then-wife Talulah Riley and asked which day would be the "wildest party"; according to the emails, the visit did not take place after Epstein later cancelled the plans.[m]

On Christmas day in 2012, Musk emailed Epstein asking "Do you have any parties planned? I've been working to the edge of sanity this year and so, once my kids head home after Christmas, I really want to hit the party scene in St Barts or elsewhere and let loose. The invitation is much appreciated, but a peaceful island experience is the opposite of what I'm looking for".[484] Epstein replied that the "ratio on my island" might make Musk's wife uncomfortable to which Musk responded, "Ratio is not a problem for Talulah".[484]

On September 11, 2013, Epstein sent an email asking Musk if he had any plans for coming to New York for the opening of the United Nations General Assembly, saying that many "interesting people" would be coming to Epstein's house. Musk responded that "Flying to NY to see UN diplomats do nothing would be an unwise use of time".[486] Epstein responded by stating "Do you think i [sic] am retarded. Just kidding, there is no one over 25 and all very cute."[486]

Musk has denied any close relationship with Epstein and described him as a "creep" who attempted to ingratiate himself with influential people.[481] When Musk was asked in 2019 if he introduced Epstein to Mark Zuckerberg, Musk responded: "I don't recall introducing Epstein to anyone, as I don't know the guy well enough to do so."[486] The released emails nonetheless showed cordial exchanges on a range of topics, including Musk's inquiry about parties on the island.[484][487][481] The correspondence also indicated that Musk suggested hosting Epstein at SpaceX, while Epstein separately discussed plans to tour SpaceX and bring "the girls", though there is no evidence that such a visit occurred.[488] Musk has described the release of the files a "distraction", later accusing the second Trump administration of suppressing them to protect powerful individuals, including Trump himself.[n]

Private jet
Main articles: ElonJet and 2022 Twitter suspensions
Musk uses a private jet owned by Falcon Landing LLC, a SpaceX-linked company, and acquired a second jet in August 2020.[492][493] His heavy use of the jets and the consequent fossil fuel usage have received criticism.[492][494] Musk's flight usage is tracked on social media through ElonJet.[495][496][497] In December 2022, Musk banned the ElonJet account on Twitter, and made temporary bans on the accounts of journalists that posted stories regarding the incident, including Donie O'Sullivan, Keith Olbermann, and journalists from The New York Times, The Washington Post, CNN, and The Intercept.[498]

Wealth
These paragraphs are an excerpt from Wealth of Elon Musk.edit
Elon Musk is the wealthiest person in the world in terms of financial assets, with an estimated net worth of US$845 billion according to the Bloomberg Billionaires Index[499] and $849.7 billion according to Forbes,[500] as of November 8, 2026, primarily from his ownership stakes of 42% of SpaceX[501] and 20% of Tesla.[502] He is eligible to receive additional Tesla[503] and SpaceX[504] equity awards subject to certain conditions.

Musk was first listed on the Forbes list of The World's Billionaires in 2012, with a net worth of $2 billion.[505] According to Forbes, his net worth reached $300 billion in 2021; $400bn in December 2024;[506] $500bn in October 2025;[507] $600bn[508] and $700bn[509] in December 2025; $800bn in February 2026;[510] and $900bn in June 2026, and he became the only trillionaire in terms of US dollars that month upon the initial public offering (IPO) of SpaceX.[511][512][513] Since then, his net worth has been volatile, largely because of changes in SpaceX’s valuation. His net worth reached an intraday peak of $1.45 trillion in the week after the IPO,[514] but by late July 2026, a SpaceX stock collapse had reduced this net worth by $750 billion, the largest net worth loss in history.[515][516][517]

In May 2020, Musk pledged to sell almost all physical possessions and said he would "own no house",[518] but in February 2026, The New York Times identified at least 37 companies that own properties which appear to be for Musk's personal use, including expensive condominiums, planes used by him for private travel and at least 1000 acres of land.[519] His wealth is managed by Excession LLC, his family office, which has been run by Jared Birchall since 2016.[520]

Musk Foundation
Main article: Musk Foundation
The Musk Foundation is a United States–based charitable foundation funded and directed primarily by Musk. The foundation is dedicated to promoting renewable energy, crewed space exploration, pediatrics, science and engineering education, and the "development of safe artificial intelligence for the benefit of humanity".[521]

Since 2020, donations have largely been sent to organizations affiliated with Musk and his businesses. At the end of 2024, the Musk Foundation had over $14 billion in assets.[522]

Public image
Main article: Public image of Elon Musk

Musk with President Donald Trump in May 2025
Although his ventures have been highly influential within their separate industries starting in the 2000s, Musk only became a public figure in the early 2010s. He has been described as an eccentric who makes spontaneous and impactful decisions, while also often making controversial statements, contrary to other billionaires who prefer reclusiveness to protect their businesses. Musk's actions and his expressed views have made him a polarizing figure.[523] Biographer Ashlee Vance described people's opinions of Musk as polarized due to his "part philosopher, part troll" persona on Twitter.[524] He has drawn denouncement for using his platform to mock the self-selection of personal pronouns,[525] while also receiving praise for bringing international attention to matters like British survivors of grooming gangs.[526]

Musk has been described as an American oligarch due to his extensive influence over public discourse, social media, industry, politics, and government policy.[527] After Trump's re-election, Musk's influence and actions during the transition period and the second presidency of Donald Trump led some to call him "President Musk", the "actual president-elect", "shadow president" or "co-president".[528][529]

Accolades
Main article: List of awards and honors received by Elon Musk
Musk with a medal
Musk receiving the National Medal of Science by President Donald Trump in 2026
Awards for his contributions to the development of the Falcon rockets include the American Institute of Aeronautics and Astronautics George Low Transportation Award in 2008,[530] the Fédération Aéronautique Internationale Gold Space Medal in 2010,[531] and the Royal Aeronautical Society Gold Medal in 2012.[532] In 2015, he received an honorary doctorate in engineering and technology from Yale University[533] and an Institute of Electrical and Electronics Engineers Honorary Membership.[534] Musk was elected a Fellow of the Royal Society (FRS) in 2018.[535][o] In 2022, Musk was elected to the National Academy of Engineering.[537]

Time has listed Musk as one of the most influential people in the world in 2010,[538] 2013,[539] 2018,[540] and 2021.[541] Musk was selected as Time's "Person of the Year" for 2021. Then Time editor-in-chief Edward Felsenthal wrote that, "Person of the Year is a marker of influence, and few individuals have had more influence than Musk on life on Earth, and potentially life off Earth too.
"""
    summary_template = """ Given the information {information} I want you to do two things
    1. summarize the information
    2. Give me two interesting things"""
    summary_prompt_template = PromptTemplate(
        import_variables=("information"), template = summary_template
    )
    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest", api_key=os.environ.get("GEMINI_API_KEY"))
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
