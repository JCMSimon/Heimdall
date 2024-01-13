class datapoints:
	""" Keeps all supported data types\n
		Examples in the 2nd line are not always exhaustive
	"""		
	undefined = "Undefined"
	" Any data that does not fit into any other datapoint "
	class _internal:
		" DO NOT USE "
		is_root_node = "Root node"
		" INTERNAL USE ONLY! No Plugin should use this. "
	class name:
		title = "Title"
		" 'Dr.', 'Mr.', 'Ms.' "
		first_name = "First name"
		" 'Mark' 'Susan' "
		middle_name = "Middle name"
		" 'Andrew' 'Anne' "
		last_name = "Last name"
		" 'Smith' 'Langley' "
		full_name = "Full name"
		" 'Dr. Mark Andrew Smith', 'Ms. Susan Anne Langley' "
	class age:
		class text:
			age = "Age (text)"
			""" 'Twenty-six', 'Sixty-five'\n
			as in Twenty-six/Sixty-five years old"""
		class numeric:
			age = "Age (numeric)"
			""" '26', '65'\n
			as in 26/65 years old"""
	class date_of_birth:
		generic = "Date of Birth"
		""" '1st of March 20250', '12.05.2005', '15th March' \n
		If possible use the more specific datapoints"""
		class text:
			day = "Day of Birth (text)"
			" 'First', '1st', 'Second', '2nd', 'Twenty-third', '23rd' "
			month = "Month of Birth (text)"
			" 'March', 'April' "
		class numeric:
			day = "Day of Birth (numeric)"
			" '1' '2' '23' "
			month = "Month of Birth (numeric)"
			" '03', '04' "
			year = "Year of Birth (numeric)"
			" '2005', '2008' "
	class person:
		pronoun = "Pronoun"
		" 'He', 'She', 'They' "
		ethnicity = "Ethnicity"
		" 'Black', 'White', 'Asian', 'Hispanic' "
		nationality = "Nationality"
		" 'American', 'Canadian', 'Russian' "
		gender = "Gender"
		" 'Male', 'Female', 'Other', etc "
		class body:
			class height:
				cm = "Height (cm)"
				" '178', '154' "
				feet = "Height (ft)"
				" '5', '4' "
				inches = "Height (Inch)"
				" '60', '75' "
			class weight:
				kg = "Weight (kg)"
				" '95', '78' "
				pounds = "Weight (lbs)"
				" '140', '150' "
			bio_gender = "Gender (bio)"
			" 'Male', 'Female', 'Other', etc "
			eye_color = "Eye Color"
			" 'Blue', 'Brown', 'Green' "
			skin_color = "Skin Color"
			""" 'Lightest' 'Very Light' 'Light' 'Fair' 'Medium' 'Tanned' 'Brown' 'Dark Brown' 'Black'\n
				(These are suggested by GPT3.5 dont blame me lol)
			"""
			hair_color = "Hair Color"
			" 'Blonde', 'Black', 'Red', 'Green' "
	class vehicle:
		type = "Vehicle type"
		" 'Car', 'Bike', 'Plane', 'Boat' "
		color = "Vehicle color"
		" 'black', 'red', 'blue', 'green' "
		brand = "Vehicle Brand"
		" 'BMW', 'Kia', etc "
		build_year = "Vehicle build year"
		" '1989', '2010' "
		class identifier:
			license_plate = "License plate"
			"""For Cars, bikes etc\n
			'SAM 911E', 'HH 07194' """
			tail_number = "Tail number"
			"""For Planes\n
			'7T-WHM	', 'N16-100	' """
			hull_identification_number = "Hull Identification Number (HIN)"
			"""For Boats\n
			'ABC12345D404'"""
	class location:
		latitude = "Latitude"
		" '37.275036', '37°16'30.1\"N' "
		longitude = "Longitude"
		" '-115.799632', '115°47'58.7\"W' "
		zip_code = "Zip code"

		state_or_region = "State/Region"
		" 'Kansas', 'Pest', 'Bayern', "
		city = "City"
		" 'Manhattan', 'Monor', 'München' "
		street = "Street"
		" 'Claflin Rd', 'Kossuth Lajos u.', 'Adelheidstraße' "
		house_number = "House number"
		" '1800 ', '74', '14' "
		class country:
			name = "Country name"
			" 'Germany', 'Hungary', 'United States of America' "
			code = "Country code"
			" 'DE', 'HU', 'USA' "
	class email:
		generic = "Generic Email"
		" '*@*.*' "
		gmail = "Gmail"
		" '*@gmail.com' "
		hotmail = "Hotmail"
		" '*@hotmail.com', '*@hotmail.co.uk', '*@hotmail.fr' "
		outlook = "Outlook mail"
		" '*@outlook.com' "
		proton = "Proton Mail"
		" '*@proton.me', '*@protonmail.com', '*pm.me' '*@protonmail.ch' "
		yahoo = "Yahoo Mail"
		" '*@yahoo.com', '*@yahoo.fr', '*@myyahoo.com' "
		aol = "AOL Email"
		" '*@aol.com' "
		msn = "MSN Email"
		" '*@msn.com' "
		# TODO | Expand list using https://email-verify.my-addr.com/list-of-most-popular-email-domains.php
	class ip:
		address_v4 = "Ip Address (v4)"
		" '192.168.123.132' "
		address_v6 = "Ip Address (v6)"
		" '0000:0000:0000:0000:0000:ffff:c0a8:7b84' "
		port = "Port"
		" '8080', 25565 "
	class hash:
		generic = "Generic hash"
		" Any hash that does not have a dedicated datapoint "
		md5 = "MD5 hash"
		" '8ce21631012f107953cb2f1bcf3dad29' "
		sha1 = "SHA-1 hash"
		" 'cfb9a5cb56f4b910863ed7a4a671ced2c17f5807' "
		sha256 = "SHA-256 hash"
		" 'ebab140b3fb81566002d832257eef15795545dbca18f679d3cb800de1da80b15' "
		bcrypt = "bcrypt hash"
		" '$2y$10$S2VvQQ9aqSLdNVPqvsYAteApDyQcH6YLO0qWUqqrBD2CWpqml/Pnq' "
		argon2i = "argon2i hash"
		" '$argon2i$v=19$m=16,t=2,p=1$SGVpbWRhbGw$kXV2SueEXeBeBpkEex6MsA' "
	class profile:
		class discord:
			class _badges:
				""" DO NOT USE AS ACTUAL DATAPOINT \n
				This class is used to standartize discord badge representation """
				active_developer = 0
				class hype_squad:
					brilliance = 0
				# TODO | Add all Discord Badges
			id = "Discord User id"
			" '155149108183695360' "
			username = "Discord Username"
			" 'Dyno' "
			old_tag = "Discord tag (#)"
			" 'Dyno#3861' "
			pfp_url = "Discord avatar"
			" 'https://cdn.discordapp.com/avatars/155149108183695360/19a5ee4114b47195fcecc6646f2380b1.png' "
			banner_url = "Discord banner"
			" 'https://cdn.discordapp.com/banners/204683417445466112/a6ca48aad51922940e6bc383dbd0d852.png' "
			bio = "Discord bio"
			""" Replace new lines with escaped new lines \n
			'The Discord bot to make server management and moderation easy. Follow your favorite streamers, run giveaways, and more! \\n \\n https://dyno.gg/' """
			badges = "Discord user badges"
			""" Refer to datapoints.socialmedia.discord._badges for a list of all supported badges \n
			'[datapoints.socialmedia.discord._badges.active_developer,datapoints.socialmedia.discord._badges.hype_squad.brilliance]' """
		class youtube:
			alias = "Youtube alias"
			" '@JCMS_', '@Miimii' "
			channel_id = "Youtube channel id"
			" 'UC3jv2yNiKPOZoWLLflNOzvg', 'UCOAmvK5o2JmH0vXi3Ql_qWg' "
			subscriber_count = "Youtube subscriber count"
			" '125', '31364', '2135949' "
			view_count = "Youtube view count (global)"
			" '438', '46228', '2649476' "
			video_count = "Youtube video count"
			" '268', '56', '1068' "
			community_post_count = "Youtube communty post count"
			" '125', '56', '1068' "
			playlist_count = "Youtube playlist count"
			" '125', '56', '1068' "
			bio = "Youtube bio"
			""" Replace new lines with escaped new lines \n
			'Welcome back to my channel!' """
		# class facebook:
		# class instagram:
		# class snapchat:
		# class threads:
		# class pinterest:
		# class chessdotcom:
		# class riotgames:
		# class namemc:
		# class doxbin:
		# class twoDimensions:
		# class threednews:
		# class sevenCups:
		# class eighttracks:
		# class nineGAG:
		# class aPClips:
		# class about.me:
		# class academia.edu:
		# class admireMe.Vip:
		# class airPilotLife:
		# class airbit:
		# class airliners:
		# class alik:
		# class allMyLinks:
		# class anilist:
		# class archiveofOurOwn:
		# class artStation:
		# class askFedora:
		# class askFM:
		# class audiojungle:
		# class autofrage:
		# class avizo:
		# class bLIPfm:
		# class bOOTH:
		# class bandcamp:
		# class bazarcz:
		# class behance:
		# class biggerPockets:
		# class bikemap:
		# class bioHacking:
		# class bitBucket:
		# class bitwardenForum:
		# class blogger:
		# class bodyBuilding:
		# class bookcrossing:
		# class braveCommunity:
		# class buyMeACoffee:
		# class buzzFeed:
		# class cNET:
		# class cTAN:
		# class caddyCommunity:
		# class carTalkCommunity:
		# class carbonmade:
		# class careerhabr:
		# class championat:
		# class chaos:
		# class chatujmecz:
		# class choiceCommunity:
		# class clapper:
		# class cloudflareCommunity:
		# class codecademy:
		# class codechef:
		# class codeforces:
		# class codepen:
		# class codersRank:
		# class coinvote:
		# class colourLovers:
		# class contently:
		# class coroflot:
		# class cracked:
		# class crevado:
		# class crowdin:
		# class cryptomatorForum:
		# class dEVCommunity:
		# class dMOJ:
		# class dailyMotion:
		# class dealabs:
		# class discogs:
		# class discussElasticco:
		# class disqus:
		# class docker Hub:
		# class dribbble:
		# class duolingo:
		# class eintrachtFrankfurtForum:
		# class envatoForum:
		# class erome:
		# class etsy:
		# class euw:
		# class exposure:
		# class eyeEm:
		# class f3cool:
		# class fameswap:
		# class fandom:
		# class finanzfrage:
		# class fiverr:
		# class flickr:
		# class flightradar24:
		# class flipboard:
		# class football:
		# class forumOphilia:
		# class fosstodon:
		# class freelance.habr:
		# class freelancer:
		# class freesound:
		# class g2G:
		# class gNOMEVCS:
		# class gaiaOnline:
		# class gamespot:
		# class geeksforGeeks:
		# class geniusArtists:
		# class geniusUsers:
		# class gesundheitsfrage:
		# class getMyUni:
		# class giantBomb:
		# class giphy:
		# class gitBook:
		# class gitHub:
		# class gitLab:
		# class gitee:
		# class goodReads:
		# class gradle:
		# class grailed:
		# class gravatar:
		# class gumroad:
		# class gutefrage:
		# class hEXRPG:
		# class hackTheBox:
		# class hackaday:
		# class hackerEarth:
		# class hackerNews:
		# class hackerOne:
		# class hackerRank:
		# class harvardScholar:
		# class heavyR:
		# class houzz:
		# class hubPages:
		# class hubski:
		# class iCQ:
		# class iFTTT:
		# class icons8 Community:
		# class imageFap:
		# class imgUpcz:
		# class imgur:
		# class instructables:
		# class ionic Forum:
		# class issuu:
		# class itch.io:
		# class itemfix:
		# class jellyfinWeblate:
		# class jimdo:
		# class joplinForum:
		# class kEAKR:
		# class kaggle:
		# class keybase:
		# class kik:
		# class kongregate:
		# class lOR:
		# class launchpad:
		# class leetCode:
		# class lessWrong:
		# class letterboxd:
		# class linktree:
		# class listed:
		# class liveJournal:
		# class lobsters:
		# class lolchess:
		# class lottieFiles:
		# class lushStories:
		# class mMORPGForum:
		# class mapify:
		# class medium:
		# class memrise:
		# class minecraft:
		# class mixCloud:
		# class modelhub:
		# class monkeytype:
		# class motherless:
		# class motorradfrage:
		# class myAnimeList:
		# class myMiniFactory:
		# class myspace:
		# class nICommunityForum:
		# class needrom:
		# class nextcloud Forum:
		# class nightbot:
		# class ninjaKiwi:
		# class nintendoLife:
		# class nitroType:
		# class notABug.org:
		# class nyaa.si:
		# class oGUsers:
		# class openStreetMap:
		# class opensource:
		# class ourDJTalk:
		# class pSNProfilescom:
		# class packagist:
		# class pastebin:
		# class patreon:
		# class periscope:
		# class pinkbike:
		# class pocketStars:
		# class polarsteps:
		# class polygon:
		# class polymart:
		# class pornhub:
		# class productHunt:
		# class promoDJ:
		# class rajcenet:
		# class rateYourMusic:
		# class rclone Forum:
		# class redTube:
		# class redbubble:
		# class reddit:
		# class reisefrage:
		# class replitcom:
		# class researchGate:
		# class reverbNation:
		# class roblox:
		# class rocketTube:
		# class rubyGems:
		# class rumble:
		# class runeScape:
		# class sWAPD:
		# class sbazarcz:
		# class scratch:
		# class scribd:
		# class shitpostBot5000:
		# class shpock:
		# class sketchfab:
		# class slant:
		# class slideShare:
		# class slides:
		# class smule:
		# class soundCloud:
		# class sourceForge:
		# class speedruncom:
		# class splice:
		# class sporcle:
		# class sportlerfrage:
		# class sportsRU:
		# class spotify:
		# class starCitizen:
		# class steamGroup:
		# class strava:
		# class sublimeForum:
		# class tLDRLegal:
		# class tRAKTRAIN:
		# class telegram:
		# class tellonymme:
		# class tenor:
		# class themeForest:
		# class tikTok:
		# class tnAFlix:
		# class tradingView:
		# class trakt:
		# class trashboxRU:
		# class trawelling:
		# class trello:
		# class tryHackMe:
		# class tuna:
		# class twitch:
		# class twitter:
		# class ultimateGuitar:
		# class unsplash:
		# class vK:
		# class vSCO:
		# class velomania:
		# class venmo:
		# class vero:
		# class vimeo:
		# class virgool:
		# class virusTotal:
		# class wICGForum:
		# class warriorForum:
		# class wattpad:
		# class webNode:
		# class weblate:
		# class weebly:
		# class whonixForum:
		# class wikidot:
		# class wikipedia:
		# class windy:
		# class wix:
		# class wolframalphaForum:
		# class wordPressOrg:
		# class wordnik:
		# class xboxGamertag:
		# class xvideos:
		# class youNow:
		# class youPic:
		# class zhihu:
		# class akniga:
		# class authorSTREAM:
		# class babyRU:
		# class babyblogRU:
		# class chaossocial:
		# class couchsurfing:
		# class d3RU:
		# class devRant:
		# class drive2:
		# class eGPU:
		# class fl:
		# class forumguns:
		# class freecodecamp:
		# class geocaching:
		# class gfycat:
		# class habr:
		# class hunting:
		# class iMGSRCRU:
		# class igromania:
		# class interpals:
		# class irecommend:
		# class jbzdcompl:
		# class kwork:
		# class labpentestit:
		# class lastfm:
		# class leasehackr:
		# class livelib:
		# class mastodoncloud:
		# class mastodonsocial:
		# class mastodontechnology:
		# class mastodonxyz:
		# class metacritic:
		# class moikrug:
		# class mstdnio:
		# class nairalandcom:
		# class nnRU:
		# class note:
		# class npm:
		# class opennet:
		# class osu!:
		# class phpRU:
		# class pikabu:
		# class pr0gramm:
		# class proghu:
		# class queeraf:
		# class satsisRU:
		# class sessionize:
		# class skyrock:
		# class socialtchncsde:
		# class spletnik:
		# class svidbook:
		# class toster:
		# class uid:
		# class wikivg:
			
	# class sensetive_data:
	# 	social_security_number = "dp.sensetive_data.social_security_number"
	# class credit_card:
	# 	name = "Credit card holder"
	# 	expiry_date = "Credit card "
	# 	expiry_month = "dp.sensetive_data.credit_card.expiry_month"
	# 	expiry_number = "dp.sensetive_data.credit_card.expiry_number"
	# 	expiry_year = "dp.sensetive_data.credit_card.expiry_year"
	# 	cvc = "dp.sensetive_data.credit_card.cvc"

	# class personal_website:
	# 	name = "dp.personal_website.name"
	# 	domain = "dp.personal_website.domain"
	# 	ip = "dp.personal_website.ip"
	# 	subdomain = "dp.personal_website.subdomain"
	# 	dns_server = "dp.personal_website.dns_server"
	# class credentials:
	# 	numerical_pin_number = "dp.credentials.numerical_pin_number"
	# 	password = "dp.credentials.password"
	# class contact:
	# 	fax_number = "dp.contact.fax_number"
	# 	phone_number = "dp.contact.phone_number"
	# class image:
	# 	generic = "dp.image.generic"
	# 	face = "dp.image.face"
	# 	id = "dp.image.id"

import inspect

def getDatapointbyString(value, cls=datapoints):
	for name, attribute in cls.__dict__.items():
		if isinstance(attribute, str) and str(attribute).lower().replace(" ","") == str(value).lower().replace(" ",""):
			return attribute
		elif inspect.isclass(attribute):
			result = getDatapointbyString(value, attribute)
			if result:
				return result
	return None