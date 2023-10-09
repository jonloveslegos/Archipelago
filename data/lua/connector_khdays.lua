console.clear()
print("NOTICE: Items obtained from a chest will be in your inventory until you change rooms. THAT IS UNFIXABLE!")
print("NOTICE: Items obtained from mission clears will only send out after you return to the hub. This may change in the future.")
print("NOTICE: Mission rewards 1-3 are for normal clear, 4-5 are for full clear.")

local socket = require("socket")
local json = require('json')
require("common")

charId = 0x00
charId2 = 0x0E

mission_address = {}

start_mission_address = 0x194AE4

mission_address["1"] = 8
mission_address["2"] = 11
mission_address["3"] = 14
mission_address["4"] = 17
mission_address["5"] = 20

local i = 0
while i < 93 do
    mission_address[tostring(i+1)] = 9 + (3 * i)
    i = i + 1
end

function hex2bin(str)
    local map = {
        ['0'] = '0000',
        ['1'] = '0001',
        ['2'] = '0010',
        ['3'] = '0011',
        ['4'] = '0100',
        ['5'] = '0101',
        ['6'] = '0110',
        ['7'] = '0111',
        ['8'] = '1000',
        ['9'] = '1001',
        ['A'] = '1010',
        ['B'] = '1011',
        ['C'] = '1100',
        ['D'] = '1101',
        ['E'] = '1110',
        ['F'] = '1111'
    }
    return str:gsub('[0-9A-F]', map)
end

function bin2hex(str)
    local map = {
        ['0000'] = '0',
        ['0001'] = '1',
        ['0010'] = '2',
        ['0011'] = '3',
        ['0100'] = '4',
        ['0101'] = '5',
        ['0110'] = '6',
        ['0111'] = '7',
        ['1000'] = '8',
        ['1001'] = '9',
        ['1010'] = 'A',
        ['1011'] = 'B',
        ['1100'] = 'C',
        ['1101'] = 'D',
        ['1110'] = 'E',
        ['1111'] = 'F',
        [' '] = ' '
    }
    local mystr = ""
    local i = 0
    while i < string.len(str) do
        local e = 0
        local temptemp = ""
        while e < 4 do
            i = i + 1
            local c = str:sub(i,i)
            if c ~= " " then
                temptemp = temptemp..c
                e = e + 1
            else
                mystr = mystr.." "
            end
        end
        mystr = mystr..map[temptemp]
    end
    return mystr
end

function strhex2array(str)
    local myarr = {}
    local i = 0
    local e = 1
    local temptemp = ""
    while i < string.len(str) do
        i = i + 1
        local c = str:sub(i,i)
        if c ~= " " then
            temptemp = temptemp..c
        else
            myarr[e] = tonumber(temptemp, 16)
            e = e + 1
            temptemp = ""
        end
    end
    myarr[e] = tonumber(temptemp, 16)
    e = e + 1
    temptemp = ""
    return myarr
end

function replace_str_ind(str, ind, char)
    return str:sub(1,ind-1)..char..str:sub(ind+1)
end

function read_mission_values()
    local hex_string = ""
    local mem = mainmemory.read_bytes_as_array(0x194AE4, 0x24)
    local myarr = {}
    local i = 1
    local e = 1
    local temptemp = ""
    while i < #mem do
        local e = 3
        local a = 0
        local temptemp = ""
        while e >= 0 do
            myarr[i+a] = mem[i+e]
            e = e - 1
            a = a + 1
        end
        i = i + 4
    end
    for _, v in ipairs(myarr) do
        hex_string = hex_string .. string.format("%02X ", v)
    end
    hex_string = hex_string:sub(1, -2) -- Hang head in shame, remove last " "
    return hex_string
end

char_ids = {}

char_ids[""] = 0x00
char_ids["Roxas"] = 0x00
char_ids["Axel"] = 0x01
char_ids["Xigbar"] = 0x02
char_ids["Saix"] = 0x03
char_ids["Xaldin"] = 0x04
char_ids["Sora"] = 0x05
char_ids["Demyx"] = 0x06
char_ids["Larxene"] = 0x07
char_ids["Lexaeus"] = 0x08
char_ids["Luxord"] = 0x09
char_ids["Marluxia"] = 0x0A
char_ids["Riku"] = 0x0B
char_ids["Vexen"] = 0x0C
char_ids["Xemnas"] = 0x0D
char_ids["Xion"] = 0x0E
char_ids["Zexion"] = 0x0F
char_ids["Mickey"] = 0x10
char_ids["Donald"] = 0x11
char_ids["Goofy"] = 0x12
char_ids["Dual-Wield_Roxas"] = 0x13

itemIds = {}

itemIds["Fire Recipe"] = 0x194EC3
itemIds["Fira Recipe"] = 0x194EC4
itemIds["Firaga Recipe"] = 0x194EC5
itemIds["Blizzard Recipe"] = 0x194EC6
itemIds["Blizzara Recipe"] = 0x194EC7
itemIds["Blizzaga Recipe"] = 0x194EC8
itemIds["Thunder Recipe"] = 0x194EC9
itemIds["Thundara Recipe"] = 0x194ECA
itemIds["Thundaga Recipe"] = 0x194ECB
itemIds["Aero Recipe"] = 0x194ECC
itemIds["Aerora Recipe"] = 0x194ECD
itemIds["Aeroga Recipe"] = 0x194ECE
itemIds["Cure Recipe"] = 0x194ECF
itemIds["Cura Recipe"] = 0x194ED0
itemIds["Curaga Recipe"] = 0x194ED1
itemIds["Elixir Recipe"] = 0x194EF9
itemIds["Megalixir Recipe"] = 0x194EFA

itemIds["Panel Slot"] = 0x194DC9
itemIds["Potion"] = 0x194DCA
itemIds["Hi-Potion"] = 0x194DCB
itemIds["Mega-Potion"] = 0x194DCC
itemIds["Ether"] = 0x194DCD
itemIds["Hi-Ether"] = 0x194DCE
itemIds["Mega-Ether"] = 0x194DCF
itemIds["Elixir"] = 0x194DD0
itemIds["Megalixir"] = 0x194DD1
itemIds["Panacea"] = 0x194DD2
itemIds["Limit Recharge"] = 0x194DD3

itemIds["Level Up"] = 0x194E07
itemIds["LV Doubler 5"] = 0x194E08
itemIds["LV Doubler 6"] = 0x194E09
itemIds["LV Doubler 6B"] = 0x194F8D
itemIds["LV Doubler 6C"] = 0x194F8E
itemIds["LV Doubler 6D"] = 0x194F8F
itemIds["LV Tripler 4"] = 0x194E0A
itemIds["LV Tripler 4B"] = 0x194E0B
itemIds["LV Tripler 4C"] = 0x194E0C
itemIds["LV Quadrupler 3"] = 0x194E0D
itemIds["LV Quadrupler 3B"] = 0x194E0E
itemIds["LV Quadrupler 3C"] = 0x194E0F
itemIds["Backpack"] = 0x194E23
itemIds["Pack Extender"] = 0x194E24

itemIds["Fire"] = 0x194E25
itemIds["Fira"] = 0x194E26
itemIds["Firaga"] = 0x194E27
itemIds["Blizzard"] = 0x194E28
itemIds["Blizzara"] = 0x194E29
itemIds["Blizzaga"] = 0x194E2A
itemIds["Thunder"] = 0x194E2B
itemIds["Thundara"] = 0x194E2C
itemIds["Thundaga"] = 0x194E2D
itemIds["Aero"] = 0x194E2E
itemIds["Aerora"] = 0x194E2F
itemIds["Aeroga"] = 0x194E30
itemIds["Cure"] = 0x194E31
itemIds["Cura"] = 0x194E32
itemIds["Curaga"] = 0x194E33
itemIds["Magic LV2 4"] = 0x194E34
itemIds["Magic LV2 4B"] = 0x194E35
itemIds["Magic LV2 4C"] = 0x194E36
itemIds["Magic LV3 4"] = 0x194E37
itemIds["Magic LV3 4B"] = 0x194E38
itemIds["Magic LV4 4"] = 0x194E39
itemIds["Doublecast 4"] = 0x194E3A
itemIds["Triplecast 3"] = 0x194E3B
itemIds["Quadcast 3"] = 0x194E3C

itemIds["Dodge Roll"] = 0x194E3D
itemIds["Dodge Roll 3"] = 0x194E3E
itemIds["Dodge Roll LV+"] = 0x194E3F
itemIds["Dodge Rush"] = 0x194E40
itemIds["Dodging Deflect"] = 0x194F88
itemIds["Dodge Combo"] = 0x194E41
itemIds["Auto-Dodge"] = 0x194E42
itemIds["Block 2"] = 0x194E43
itemIds["Block 4"] = 0x194E44
itemIds["Block LV+"] = 0x194E45
itemIds["Perfect Block"] = 0x194E46
itemIds["Block-Counter"] = 0x194E47
itemIds["Block-Retreat"] = 0x194E48
itemIds["Sliding Block"] = 0x194E49
itemIds["Block-Jump"] = 0x194E4A
itemIds["Fire Block"] = 0x194E4B
itemIds["Blizzard Block"] = 0x194E4C
itemIds["Thunder Block"] = 0x194E4D
itemIds["Aero Block"] = 0x194E4E
itemIds["Block Bonus"] = 0x194E4F
itemIds["Round Block"] = 0x194E50
itemIds["Auto-Block"] = 0x194E51
itemIds["Aerial Recovery"] = 0x194E5C
itemIds["Aerial Recovery 3"] = 0x194E5D
itemIds["A. Recovery LV+"] = 0x194E5E
itemIds["Quick Recovery"] = 0x194E5F
itemIds["Aerial Payback"] = 0x194E60
itemIds["Smash Recovery"] = 0x194E61
itemIds["Air Slide 2"] = 0x194E58
itemIds["Air Slide 5"] = 0x194E59
itemIds["Air Slide LV+"] = 0x194E5A
itemIds["Air Rush"] = 0x194E5B
itemIds["Sliding Dash"] = 0x194E62
itemIds["Sliding Dash 3"] = 0x194E63
itemIds["Sliding Dash LV+"] = 0x194E64
itemIds["Glide 3"] = 0x194E52
itemIds["Glide 5"] = 0x194E53
itemIds["Glide LV+"] = 0x194E54
itemIds["Homing Glide"] = 0x194E56
itemIds["Rocket Glide"] = 0x194E57
itemIds["Haste"] = 0x194E65
itemIds["Haste 3"] = 0x194E66
itemIds["Haste LV+"] = 0x194E67
itemIds["High Jump"] = 0x194E68
itemIds["High Jump 3"] = 0x194E69
itemIds["High Jump LV+"] = 0x194E6A
itemIds["Float"] = 0x194E6B
itemIds["Treasure Magnet"] = 0x194E7C
itemIds["Treasure Magnet 3"] = 0x194E7D
itemIds["Treasure Magnet LV+"] = 0x194E7E
itemIds["Auto-Life 3"] = 0x194E6C
itemIds["Auto-Life LV+"] = 0x194E6D
itemIds["Limit Boost"] = 0x194E85
itemIds["Final Limit"] = 0x194F89
itemIds["Scan"] = 0x194E84
itemIds["Range Extender"] = 0x194E83
itemIds["Auto-Lock"] = 0x194E86
itemIds["Ultima Weapon"] = 0x194F87

itemIds["Skill Gear"] = 0x194E88
itemIds["Skill Gear+ 2"] = 0x194E89
itemIds["Technical Gear 3"] = 0x194E8F
itemIds["Technical Gear+ 3"] = 0x194E90
itemIds["Duel Gear 4"] = 0x194E9B
itemIds["Duel Gear+ 4"] = 0x194E9A
itemIds["Duel Gear++ 5"] = 0x194EA4
itemIds["Loaded Gear"] = 0x194E8A
itemIds["Loaded Gear+ 2"] = 0x194E8B
itemIds["Chrono Gear 3"] = 0x194E91
itemIds["Chrono Gear+ 3"] = 0x194E92
itemIds["Phantom Gear 4"] = 0x194E9C
itemIds["Phantom Gear+ 4"] = 0x194E9D
itemIds["Phantom Gear++ 5"] = 0x194EA5
itemIds["Lift Gear 3"] = 0x194E95
itemIds["Lift Gear+ 3"] = 0x194E96
itemIds["Nimble Gear 4"] = 0x194EA1
itemIds["Nimble Gear+ 4"] = 0x194EA0
itemIds["Wild Gear 3"] = 0x194E97
itemIds["Wild Gear+ 3"] = 0x194E98
itemIds["Ominous Gear 4"] = 0x194EA3
itemIds["Ominous Gear+ 4"] = 0x194EA2
itemIds["Valor Gear 2"] = 0x194E8C
itemIds["Valor Gear+ 2"] = 0x194E8D
itemIds["Fearless Gear 3"] = 0x194E93
itemIds["Fearless Gear+ 3"] = 0x194E94
itemIds["Prestige Gear 4"] = 0x194E9F
itemIds["Prestige Gear+ 4"] = 0x194E9E
itemIds["Crisis Gear 5"] = 0x194EA8
itemIds["Crisis Gear+ 5"] = 0x194EA9
itemIds["Omega Gear 6"] = 0x194EB2
itemIds["Omega Gear+ 6"] = 0x194EB1
itemIds["Hazard Gear 5"] = 0x194EA6
itemIds["Hazard Gear+ 5"] = 0x194EA7
itemIds["Rage Gear 5"] = 0x194EAD
itemIds["Rage Gear+ 5"] = 0x194EAC
itemIds["Champion Gear 5"] = 0x194EAA
itemIds["Champion Gear+ 5"] = 0x194EAB
itemIds["Ultimate Gear 6"] = 0x194EB4
itemIds["Ultimate Gear+ 6"] = 0x194EB3
itemIds["Pandora's Gear 5"] = 0x194EB0
itemIds["Pandora's Gear+ 5"] = 0x194EAF
itemIds["Zero Gear 5"] = 0x194EAE
itemIds["Casual Gear 2"] = 0x194E8E
itemIds["Mystery Gear 3"] = 0x194E99
itemIds["Ability Unit"] = 0x194EB9
itemIds["Power Unit"] = 0x194EBF
itemIds["Magic Unit"] = 0x194EC1
itemIds["Guard Unit"] = 0x194EC0
itemIds["Sight Unit"] = 0x194EC2


itemIds["Sign of Resolve"] = 0x194F92
itemIds["Brawl Ring"] = 0x194F93
itemIds["Magic Ring"] = 0x194F94
itemIds["Soldier Ring"] = 0x194F95
itemIds["Fencer's Ring"] = 0x194F96
itemIds["Fire Charm"] = 0x194F97
itemIds["Flower Charm"] = 0x194F98
itemIds["Strike Ring"] = 0x194F99
itemIds["Lucky Ring"] = 0x194F9A
itemIds["Blizzard Charm"] = 0x194F9B
itemIds["White Ring"] = 0x194F9C
itemIds["Knight's Defense"] = 0x194F9D
itemIds["Raider's Ring"] = 0x194F9E
itemIds["Thunder Charm"] = 0x194F9F
itemIds["Recovery Ring"] = 0x194FA0
itemIds["Vitality Ring"] = 0x194FA1
itemIds["Rainforce Ring"] = 0x194FA2
itemIds["Double Up"] = 0x194FA3
itemIds["Storm's Eye"] = 0x194FA4
itemIds["Critical Ring"] = 0x194FA5
itemIds["Fairy Circle"] = 0x194FA6
itemIds["Full Circle"] = 0x194FA7
itemIds["Lucky Star"] = 0x194FA8
itemIds["Charge Ring"] = 0x194FA9
itemIds["Eternal Ring"] = 0x194FAA
itemIds["Carmine Blight"] = 0x194FAB
itemIds["Frozen Blight"] = 0x194FAC
itemIds["Safety Ring"] = 0x194FAD
itemIds["Princess's Crown"] = 0x194FAE
itemIds["Lunar Strike"] = 0x194FAF
itemIds["Crimson Blood"] = 0x194FB0
itemIds["Deep Sky"] = 0x194FB1
itemIds["Protect Ring"] = 0x194FB2
itemIds["Might Crown"] = 0x194FB3
itemIds["Critical Sun"] = 0x194FB4
itemIds["Three Stars"] = 0x194FB5
itemIds["Imperial Crown"] = 0x194FB6
itemIds["Witch's Chaos"] = 0x194FB7
itemIds["Rune Ring"] = 0x194FB8
itemIds["Extreme"] = 0x194FB9
itemIds["Master's Circle"] = 0x194FBA
itemIds["Nothing to Fear"] = 0x194FC7
itemIds["Space in Its Place"] = 0x194FBB
itemIds["Flagging Winds"] = 0x194FBC
itemIds["Ice Breaker"] = 0x194FBD
itemIds["Down to Earth"] = 0x194FBE
itemIds["Lose Your Illusion"] = 0x194FBF
itemIds["Sighing of the Moon"] = 0x194FC0
itemIds["Tears of Flame"] = 0x194FC1
itemIds["Parting of Waters"] = 0x194FC2
itemIds["Test of Time"] = 0x194FC3
itemIds["Flowers Athirst"] = 0x194FC4
itemIds["Stolen Thunder"] = 0x194FC5
itemIds["Dying of the Light"] = 0x194FC6

synth = {}
for k, v in pairs(itemIds) do
    synth[k] = 0
end
itemMax = {}
for k, v in pairs(itemIds) do
    itemMax[k] = 1
end
itemMax["Panel Slot"] = 1
itemMax["Potion"] = 20
itemMax["Hi-Potion"] = 99
itemMax["Mega-Potion"] = 99
itemMax["Ether"] = 20
itemMax["Hi-Ether"] = 99
itemMax["Mega-Ether"] = 99
itemMax["Elixir"] = 99
itemMax["Megalixir"] = 99
itemMax["Panacea"] = 99
itemMax["Limit Recharge"] = 99
itemMax["Level Up"] = 1
itemMax["Backpack"] = 99
itemMax["Fire"] = 2
itemMax["Fira"] = 99
itemMax["Firaga"] = 99
itemMax["Blizzard"] = 2
itemMax["Blizzara"] = 99
itemMax["Blizzaga"] = 99
itemMax["Thunder"] = 99
itemMax["Thundara"] = 99
itemMax["Thundaga"] = 99
itemMax["Aero"] = 99
itemMax["Aerora"] = 99
itemMax["Aeroga"] = 99
itemMax["Cure"] = 99
itemMax["Cura"] = 99
itemMax["Curaga"] = 99
itemMax["Glide LV+"] = 99
itemMax["Treasure Magnet LV+"] = 99
itemMax["Auto-Life LV+"] = 99
itemMax["Air Slide LV+"] = 99
itemMax["Ability Unit"] = 99
itemMax["Power Unit"] = 99
itemMax["Guard Unit"] = 99
itemMax["Magic Unit"] = 99
itemMax["Sight Unit"] = 99
itemMax["Block LV+"] = 99
itemMax["A. Recovery LV+"] = 99
itemMax["Sliding Dash LV+"] = 99
itemMax["Haste LV+"] = 99
itemMax["High Jump LV+"] = 99
itemMax["Fire Recipe"] = 99
itemMax["Fira Recipe"] = 99
itemMax["Firaga Recipe"] = 99
itemMax["Blizzard Recipe"] = 99
itemMax["Blizzara Recipe"] = 99
itemMax["Blizzaga Recipe"] = 99
itemMax["Thunder Recipe"] = 99
itemMax["Thundara Recipe"] = 99
itemMax["Thundaga Recipe"] = 99
itemMax["Aero Recipe"] = 99
itemMax["Aerora Recipe"] = 99
itemMax["Aeroga Recipe"] = 99
itemMax["Cure Recipe"] = 99
itemMax["Cura Recipe"] = 99
itemMax["Curaga Recipe"] = 99
itemMax["Elixir Recipe"] = 99
itemMax["Megalixir Recipe"] = 99

slotIds = {}
slotIds[0] = 0x04C712
slotIds[1] = 0x04C716
slotIds[2] = 0x04C71A
slotIds[3] = 0x04C71E
slotIds[4] = 0x04C722
slotIds[5] = 0x04C726
slotIds[6] = 0x04C72A
slotIds[7] = 0x04C72E
slotIds[8] = 0x04C732
slotIds[9] = 0x04C736
slotIds[10] = 0x04C73A
slotIds[11] = 0x04C73E
slotIds[12] = 0x04C742
slotIds[13] = 0x04C746
slotIds[14] = 0x04C74A
slotIds[15] = 0x04C74E
slotIds[16] = 0x04C752
slotIds[17] = 0x04C756

equipSlotIds = {}
equipSlotIds[0] = 0x04C694
equipSlotIds[1] = 0x04C698
equipSlotIds[2] = 0x04C69C
equipSlotIds[3] = 0x04C6A0
equipSlotIds[4] = 0x04C6A4
equipSlotIds[5] = 0x04C6A8
equipSlotIds[6] = 0x04C6AC
equipSlotIds[7] = 0x04C6B0
equipSlotIds[8] = 0x04C6B4
equipSlotIds[9] = 0x04C6B8

chestCount = {}
ipsc = 1
while ipsc <= 93 do
    chestCount[ipsc] = 0
    ipsc = ipsc + 1
end
chestCount[1] = 1
chestCount[2] = 0
chestCount[3] = 1
chestCount[4] = 4
chestCount[5] = 1
chestCount[6] = 0
chestCount[7] = 3
chestCount[8] = 2
chestCount[9] = 7
chestCount[10] = 0
chestCount[11] = 5
chestCount[12] = 2
chestCount[13] = 1
chestCount[14] = 5
chestCount[15] = 5
chestCount[16] = 5
chestCount[17] = 2
chestCount[18] = 4
chestCount[19] = 3
chestCount[20] = 2
chestCount[21] = 8
chestCount[22] = 5
chestCount[23] = 7
chestCount[24] = 8
chestCount[25] = 2
chestCount[26] = 6
chestCount[27] = 6
chestCount[28] = 6
chestCount[29] = 7
chestCount[30] = 6
chestCount[31] = 7
chestCount[32] = 8
chestCount[33] = 0
chestCount[34] = 8
chestCount[35] = 6
chestCount[36] = 2
chestCount[37] = 0
chestCount[38] = 6
chestCount[39] = 3
chestCount[40] = 3
chestCount[41] = 3
chestCount[42] = 3
chestCount[43] = 4
chestCount[44] = 2
chestCount[45] = 4
chestCount[46] = 3
chestCount[47] = 3
chestCount[48] = 8
chestCount[49] = 8
chestCount[50] = 4

sentIds = {}

obtainedCount = {}
hasCount = {}
sentMissionCount = {}
ipsc = 1
while ipsc <= 93 do
    sentMissionCount[ipsc] = 0
    ipsc = ipsc + 1
end
moogleBuyCount = {}
moogleBuyCount = {}
for k, v in pairs(itemIds) do
    obtainedCount[k] = itemMax[k]
    hasCount[k] = 0
    moogleBuyCount[k] = 0
end
already_obtained = {}
function handle_items(itemName)
    local potion_count = mainmemory.read_u8(itemIds[itemName])
    local got_checks = {}
    if hasCount[itemName] < potion_count then
        local i = 0
        local toSend = potion_count-hasCount[itemName]
        while i < toSend do
            if moogleBuyCount[itemName] < 99 then--itemMax[itemName] then
                if mainmemory.read_u8(0x1A7F60) == 0x0C then
                    print("\"Moogle: "..itemName.." "..tostring(moogleBuyCount[itemName]+1).."\": "..tostring(((itemIds[itemName]-0x194DC9)*100)+510000+moogleBuyCount[itemName])..",")
                    got_checks[tostring(i)] = ((itemIds[itemName]-0x194DC9)*100)+510000+moogleBuyCount[itemName]
                    moogleBuyCount[itemName] = moogleBuyCount[itemName] + 1
                    mainmemory.write_u8(itemIds[itemName], mainmemory.read_u8(itemIds[itemName])-1)
                else
                    print("\"Hub: "..itemName.." "..tostring(moogleBuyCount[itemName]+1).."\": "..tostring(((itemIds[itemName]-0x194DC9)*100)+510000+moogleBuyCount[itemName])..",")
                    got_checks[tostring(i)] = ((itemIds[itemName]-0x194DC9)*100)+510000+moogleBuyCount[itemName]
                    moogleBuyCount[itemName] = moogleBuyCount[itemName] + 1
                    mainmemory.write_u8(itemIds[itemName], mainmemory.read_u8(itemIds[itemName])-1)
                end
            else
                hasCount[itemName] = hasCount[itemName] + 1
            end
            i = i + 1
        end
    end
    if already_obtained ~= nil then
        local merged = {}
        local i = 0
        for k, v in pairs(already_obtained) do
            if countEntries(merged)[v] == nil then
                merged[tostring(i)] = v
                i = i + 1
            else
                if countEntries(merged)[v] <= 0 then
                    merged[tostring(i)] = v
                    i = i + 1
                end
            end
        end
        for k, v in pairs(got_checks) do
            if countEntries(merged)[v] == nil then
                merged[tostring(i)] = v
                i = i + 1
            else
                if countEntries(merged)[v] <= 0 then
                    merged[tostring(i)] = v
                    i = i + 1
                end
            end
        end
        return merged
    else
        return got_checks
    end
end

function receive_item(itemName)
    mainmemory.write_u8(itemIds[itemName], mainmemory.read_u8(itemIds[itemName])+1)
end

local STATE_OK = "Ok"
local STATE_TENTATIVELY_CONNECTED = "Tentatively Connected"
local STATE_INITIAL_CONNECTION_MADE = "Initial Connection Made"
local STATE_UNINITIALIZED = "Uninitialized"

local prevstate = ""
local curstate =  STATE_UNINITIALIZED
local zeldaSocket = nil
local frame = 0

local hasEnteredGame = false

local hasSetup = false

function countEntries(inputTable)
    result = {} 
    for i, v in ipairs(inputTable) do
        if result[v] ~= nil then
            result[v] = result[v] + 1
        else
            result[v] = 1
        end
    end
    return result
end

function processBlock(block)
    if block ~= nil then
        local connected_to_server = block["connection"]
        if connected_to_server == "false" then
            reset_variables()
        end
        local itemsBlock = block["items"]
        isInGame = StateOKForMainLoop()
        if itemsBlock ~= nil and isInGame then
            tempCount = {}
            for k, v in pairs(itemIds) do
                tempCount[k] = 0
            end
            for i, item in pairs(itemsBlock) do
                tempCount[item] = tempCount[item] + 1
            end
            for k, v in pairs(tempCount) do
                while v > obtainedCount[k] do
                    receive_item(k)
                    obtainedCount[k] = obtainedCount[k] + 1
                    hasCount[k] = mainmemory.read_u8(itemIds[k])
                end
            end
        end
        if itemsBlock ~= nil and isInGame then
            tempCount = {}
            for k, v in pairs(itemIds) do
                tempCount[k] = 0
            end
            for i, item in pairs(itemsBlock) do
                tempCount[item] = tempCount[item] + 1
            end
            for k, v in pairs(tempCount) do
                obtainedCount[k] = v
            end
        end
        local locBlock = block["checked_locs"]
        if locBlock ~= nil then
            moogleBuyCount = {}
            for k, v in pairs(itemIds) do
                moogleBuyCount[k] = 0
            end
            for y, u in pairs(locBlock) do
                moogleBuyCount[y] = u
            end
        end
        local char1 = block["char_1"]
        if char1 ~= nil then
            charId = char_ids[char1]
        end
        local char2 = block["char_2"]
        if char2 ~= nil then
            charId2 = char_ids[char2]
        end
    end
end

function StateOKForMainLoop()
    return ((mainmemory.read_u8(0x1A7F60) == 0x07 or mainmemory.read_u8(0x1A7F60) == 0x08 or mainmemory.read_u8(0x1A7F60) == 0x0D) and (mainmemory.read_u8(0x04BD84) ~= 0x80))
end

local pastBattleItems = {}
for k, v in pairs(equipSlotIds) do
    pastBattleItems[k] = 0
end

local pastBattleIds = {}
for k, v in pairs(equipSlotIds) do
    pastBattleIds[k] = 0
end

function receive()
    l, e = zeldaSocket:receive()
    if e == 'closed' then
        if curstate == STATE_OK then
            print("Connection closed")
        end
        curstate = STATE_UNINITIALIZED
        return
    elseif e == 'timeout' then
        print("timeout")
        return
    elseif e ~= nil then
        print(e)
        curstate = STATE_UNINITIALIZED
        return
    end

    local retTable = {}
    if StateOKForMainLoop() then
        local hex_string = read_mission_values()
        local tempbin = hex2bin(hex_string)
        tempbin = tempbin:gsub(" ","")
        for _, i in pairs(mission_address) do
            if tempbin:sub(i, i) == "1" and tempbin:sub(i+1, i+1) == "1" and sentMissionCount[tonumber(_)] < 2 then
                local it = 1
                local merged = {}
                local e = 0
                for k, v in pairs(already_obtained) do
                    if countEntries(merged)[v] == nil then
                        merged[tostring(e)] = v
                        e = e + 1
                    else
                        if countEntries(merged)[v] <= 0 then
                            merged[tostring(e)] = v
                            e = e + 1
                        end
                    end
                end
                if sentMissionCount[tonumber(_)] == 1 then
                    it = 4
                end
                while it <= 5 do
                    merged[tostring(e)] = it+570000+(tonumber(_)*100)
                    print("\"Mission "..tostring(_)..": Reward "..tostring(it).."\": "..tostring(merged[tostring(e)])..",")
                    e = e + 1
                    it = it + 1
                end
                already_obtained = merged
                for itemName, __ in pairs(itemIds) do
                    if itemName ~= "Level Up" then
                        mainmemory.write_u8(itemIds[itemName], hasCount[itemName])
                    end
                end
                sentMissionCount[tonumber(_)] = 2
            else
                if tempbin:sub(i, i) == "1" and sentMissionCount[tonumber(_)] < 1 then
                    local it = 1
                    local merged = {}
                    local e = 0
                    for k, v in pairs(already_obtained) do
                        if countEntries(merged)[v] == nil then
                            merged[tostring(e)] = v
                            e = e + 1
                        else
                            if countEntries(merged)[v] <= 0 then
                                merged[tostring(e)] = v
                                e = e + 1
                            end
                        end
                    end
                    while it <= 3 do
                        merged[tostring(e)] = it+570000+(tonumber(_)*100)
                        print("\"Mission "..tostring(_)..": Reward "..tostring(it).."\": "..tostring(merged[tostring(e)])..",")
                        e = e + 1
                        it = it + 1
                    end
                    already_obtained = merged
                    for itemName, __ in pairs(itemIds) do
                        if itemName ~= "Level Up" then
                            mainmemory.write_u8(itemIds[itemName], hasCount[itemName])
                        end
                    end
                    sentMissionCount[tonumber(_)] = 1
                end
            end
        end
    end
    if (StateOKForMainLoop() or mainmemory.read_u8(0x1A7F60) == 0x0C) and hasEnteredGame then
        for k, v in pairs(itemIds) do
            already_obtained = handle_items(k)
        end
    end
    if StateOKForMainLoop() then
        if not hasEnteredGame then
            for k, v in pairs(itemIds) do
                obtainedCount[k] = mainmemory.read_u8(v)
                hasCount[k] = mainmemory.read_u8(v)
            end
        end
    end
    retTable["checked_locs"] = already_obtained
    processBlock(json.decode(l))
    if mainmemory.read_u8(0x1A7F60) == 0x54 then
        if not (mainmemory.read_u8(0x1A4978) == 255 and mainmemory.read_u8(0x1A497C) == 255) then
            retTable["day"] = tostring(mainmemory.read_u8(0x1A497C))
        end
    end
    if StateOKForMainLoop() then
        for k, v in pairs(itemIds) do
            hasCount[k] = mainmemory.read_u8(v)
        end
    end
    if mainmemory.read_u8(0x04BD84) == 0x02 then
        for k, v in pairs(equipSlotIds) do
            local index={}
            for b,c in pairs(itemIds) do
                index[tostring(c)]=b
            end
            local itemName = index[tostring(0x194DC9+pastBattleIds[k]-1)]
            if pastBattleItems[k] > mainmemory.read_u16_le(v+2) and pastBattleIds[k] > 1 then
                hasCount[itemName] = hasCount[itemName] - (pastBattleItems[k]-mainmemory.read_u16_le(v+2))
            end
            pastBattleItems[k] = mainmemory.read_u16_le(v+2)
            pastBattleIds[k] = mainmemory.read_u16_le(v)
        end
    end
    
    msg = json.encode(retTable).."\n"
    local ret, error = zeldaSocket:send(msg)
    if ret == nil then
        print(error)
    elseif curstate == STATE_INITIAL_CONNECTION_MADE then
        curstate = STATE_TENTATIVELY_CONNECTED
    elseif curstate == STATE_TENTATIVELY_CONNECTED then
        print("Connected!")
        curstate = STATE_OK
    end
    if not hasEnteredGame then
        hasEnteredGame = StateOKForMainLoop()
    end
end

function reset_variables()
    hasEnteredGame = false

    sentIds = {}
    
    obtainedCount = {}
    hasCount = {}
    moogleBuyCount = {}
    for k, v in pairs(itemIds) do
        obtainedCount[k] = 0
        hasCount[k] = 0
        moogleBuyCount[k] = 0
    end
    
    already_obtained = {}
end

currentMission = 1

inShop = false

sentMissionStuff = false
past_money = 0

function main()
    if not checkBizhawkVersion() then
        return
    end
    server, error = socket.bind('localhost', 52987)
    while true do
        frame = frame + 1
        if not (curstate == prevstate) then
            prevstate = curstate
        end
        if (curstate == STATE_OK) or (curstate == STATE_INITIAL_CONNECTION_MADE) or (curstate == STATE_TENTATIVELY_CONNECTED) then
            if mainmemory.read_u8(0x1A7F60) == 0x0C then
                for itemName, __ in pairs(itemIds) do
                    if mainmemory.read_u8(itemIds[itemName]) > hasCount[itemName] then
                        past_money = mainmemory.read_u16_le(0x1945C0)
                    end
                end
                for itemName, __ in pairs(itemIds) do
                    if mainmemory.read_u8(itemIds[itemName]) < hasCount[itemName] then
                        mainmemory.write_u16_le(0x1945C0, past_money)
                    end
                end
                past_money = mainmemory.read_u16_le(0x1945C0)
                inShop = true
            else
                if inShop then
                    for itemName, __ in pairs(itemIds) do
                        mainmemory.write_u8(itemIds[itemName], hasCount[itemName])
                    end
                end
                inShop = false
            end
            if mainmemory.read_u8(0x04BD84) == 0x02 then
                for a,b in pairs(slotIds) do
                    if mainmemory.read_u16_le(b) ~= 0x0000 then
                        local index={}
                        for k,v in pairs(itemIds) do
                            index[tostring(v)]=k
                        end
                        local itemName = index[tostring(0x194DC9+mainmemory.read_u16_le(b)-1)]
                        if itemName ~= nil then
                            if chestCount[mainmemory.read_u16_le(0x04C21C)] > mainmemory.read_u16_le(b+2) then
                                if sentIds[tostring(mainmemory.read_u16_le(b+2))] == nil then
                                    local merged = {}
                                    local e = 0
                                    for k, v in pairs(already_obtained) do
                                        if countEntries(merged)[v] == nil then
                                            merged[tostring(e)] = v
                                            e = e + 1
                                        else
                                            if countEntries(merged)[v] <= 0 then
                                                merged[tostring(e)] = v
                                                e = e + 1
                                            end
                                        end
                                    end
                                    temp = mainmemory.read_u16_le(0x04C21C)*100
                                    sentIds[tostring(mainmemory.read_u16_le(b+2))] = "done"
                                    merged[tostring(e)] = mainmemory.read_u16_le(b+2)+500000+temp
                                    print("\"Mission "..tostring(mainmemory.read_u16_le(0x04C21C))..": "..itemName.." "..tostring(mainmemory.read_u16_le(b+2)+1).."\": "..tostring(merged[tostring(e)])..",")
                                    already_obtained = merged
                                end
                                mainmemory.write_u16_le(b, 0x0000)
                            else
                                mainmemory.write_u16_le(b, 0x0000)
                                hasCount[itemName] = hasCount[itemName] + 1
                                console.clear()
                                print("Mission "..tostring(mainmemory.read_u16_le(0x04C21C))..": Obtained item higher than chest count, please report if you got this item from a chest. Moving to hub inventory for now.")
                            end
                        else
                            temp = mainmemory.read_u16_le(0x04C21C)*100
                            merged[tostring(e)] = mainmemory.read_u16_le(b+2)+500000+temp
                            print("\"Mission "..tostring(mainmemory.read_u16_le(0x04C21C))..": (UNKNOWN ITEM ID "..tostring(0x194DC9+mainmemory.read_u16_le(b)-1)..") "..tostring(mainmemory.read_u16_le(b+2)+1).."\": "..tostring(merged[tostring(e)])..",")
                        end
                    end
                end
            end
            if StateOKForMainLoop() then
                sentIds = {}
            end
            if (frame % 20 == 0) and mainmemory.read_u8(0x1A7F60) == 0x0C then
                receive()
                frame = 0
            else
                if (frame % 60 == 0) then
                    receive()
                    frame = 0
                end
            end
            if mainmemory.read_u8(0x04BD84) == 0x02 then
                mainmemory.write_u8(0x04C65B, charId)
            else
                mainmemory.write_u8(0x04C65B, 0x00)
            end
            if mainmemory.read_u8(0x04BD84) == 0x02 then
                mainmemory.write_u8(0x04C75F, charId2)
            else
                mainmemory.write_u8(0x04C75F, 0x00)
            end
        elseif (curstate == STATE_UNINITIALIZED) then
            if  (frame % 60 == 0) then
                server:settimeout(2)
                print("Attempting to connect")
                local client, timeout = server:accept()
                if timeout == nil then
                    reset_variables()
                    -- print('Initial Connection Made')
                    curstate = STATE_INITIAL_CONNECTION_MADE
                    zeldaSocket = client
                    zeldaSocket:settimeout(0)
                end
            end
        end
        emu.frameadvance()
    end
end

main()