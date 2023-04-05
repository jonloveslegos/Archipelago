console.clear()

local socket = require("socket")
local json = require('json')

charId = 0x00
charId2 = 0x00

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
char_ids["Dual-Wield Roxas"] = 0x13

itemIds = {}

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
itemMax["Panel Slot"] = 105
itemMax["Potion"] = 95
itemMax["Hi-Potion"] = 54
itemMax["Mega-Potion"] = 15
itemMax["Ether"] = 56
itemMax["Hi-Ether"] = 30
itemMax["Mega-Ether"] = 15
itemMax["Elixir"] = 10
itemMax["Megalixir"] = 5
itemMax["Panacea"] = 30
itemMax["Limit Recharge"] = 30
itemMax["Level Up"] = 39
itemMax["Backpack"] = 3
itemMax["Fire"] = 24
itemMax["Fira"] = 10
itemMax["Firaga"] = 3
itemMax["Blizzard"] = 20
itemMax["Blizzara"] = 13
itemMax["Blizzaga"] = 5
itemMax["Thunder"] = 23
itemMax["Thundara"] = 9
itemMax["Thundaga"] = 5
itemMax["Aero"] = 19
itemMax["Aerora"] = 9
itemMax["Aeroga"] = 4
itemMax["Cure"] = 22
itemMax["Cura"] = 12
itemMax["Curaga"] = 5
itemMax["Glide LV+"] = 4
itemMax["Treasure Magnet LV+"] = 2
itemMax["Auto-Life LV+"] = 2
itemMax["Air Slide LV+"] = 4
itemMax["Ability Unit"] = 3
itemMax["Power Unit"] = 5
itemMax["Guard Unit"] = 5
itemMax["Magic Unit"] = 5
itemMax["Sight Unit"] = 5
itemMax["Block LV+"] = 3
itemMax["A. Recovery LV+"] = 2
itemMax["Sliding Dash LV+"] = 2
itemMax["Haste LV+"] = 2
itemMax["High Jump LV+"] = 2

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

sentIds = {}

obtainedCount = {}
hasCount = {}
sentCount = {}
for k, v in pairs(itemIds) do
    obtainedCount[k] = 0
    hasCount[k] = 0
    sentCount[k] = 0
end

already_obtained = {}
function handle_items(itemName)
    local potion_count = mainmemory.read_u8(itemIds[itemName])
    local got_checks = {}
    if hasCount[itemName] < potion_count then
        local i = 0
        local toSend = potion_count-hasCount[itemName] + sentCount[itemName]
        while i < toSend do
            local temp = toSend-i
            if temp <= itemMax[itemName] then
                got_checks[tostring(i)] = (itemIds[itemName]*1000)-1654784000+500000+temp
            end
            i = i + 1
        end
        mainmemory.write_u8(itemIds[itemName], mainmemory.read_u8(itemIds[itemName])-(potion_count-hasCount[itemName]))
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

local itemMessages = {}
local prevstate = ""
local curstate =  STATE_UNINITIALIZED
local zeldaSocket = nil
local frame = 0

local hasEnteredGame = false

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
            sentCount = {}
            for k, v in pairs(itemIds) do
                sentCount[k] = 0
            end
            for y, u in pairs(locBlock) do
                sentCount[y] = u
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
    return mainmemory.read_u8(0x1A7F60) == 0x0C or ((mainmemory.read_u8(0x1A7F60) == 0x07 or mainmemory.read_u8(0x1A7F60) == 0x08 or mainmemory.read_u8(0x1A7F60) == 0x0D) and (mainmemory.read_u8(0x04BD84) ~= 0x80))
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

    -- Determine Message to send back
    local retTable = {}
    if StateOKForMainLoop() and hasEnteredGame then
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
        itemMessages["(0,0)"] = {TTL=240, message="Connected", color="green"}
        curstate = STATE_OK
    end
    if not hasEnteredGame then
        hasEnteredGame = StateOKForMainLoop()
    end
end

function table.empty (self)
    for _, _ in pairs(self) do
        return false
    end
    return true
end

function reset_variables()
    hasEnteredGame = false

    sentIds = {}
    
    obtainedCount = {}
    hasCount = {}
    sentCount = {}
    for k, v in pairs(itemIds) do
        obtainedCount[k] = 0
        hasCount[k] = 0
        sentCount[k] = 0
    end
    
    already_obtained = {}
end

function main()
    server, error = socket.bind('localhost', 52987)
    while true do
        frame = frame + 1
        if not (curstate == prevstate) then
            prevstate = curstate
        end
        if (curstate == STATE_OK) or (curstate == STATE_INITIAL_CONNECTION_MADE) or (curstate == STATE_TENTATIVELY_CONNECTED) then
            if mainmemory.read_u8(0x04BD84) == 0x02 then
                for a,b in pairs(slotIds) do
                    if mainmemory.read_u16_le(b) ~= 0x0000 then
                        local index={}
                        for k,v in pairs(itemIds) do
                            index[tostring(v)]=k
                        end
                        local itemName = index[tostring(0x194DC9+mainmemory.read_u16_le(b)-1)]
                        if itemName ~= nil then
                            local temp = 1 + sentCount[itemName]
                            if temp <= 200 and sentIds[tostring(mainmemory.read_u16_le(b+2))] == nil then
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
                                sentIds[tostring(mainmemory.read_u16_le(b+2))] = "done"
                                merged[tostring(e)] = ((itemIds[itemName])*1000)-1654784000+500000+temp
                                already_obtained = merged
                            end
                            mainmemory.write_u16_le(b, 0x0000)
                        end
                    end
                end
            end
            if StateOKForMainLoop() then
                sentIds = {}
            end
            if (frame % 60 == 0) then
                receive()
                frame = 0
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