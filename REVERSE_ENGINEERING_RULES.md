# Reverse Engineering Rules & Best Practices

## 📋 **VARIABLE NAMING CONVENTIONS**

### **Primary Naming Rules**
1. **Every variable MUST have a clear, descriptive name** that explains its purpose
2. **No generic names** like `var1`, `local_8`, `param_1` unless absolutely necessary
3. **Use snake_case** for consistency with C-style naming
4. **Include type hints** in names when helpful (e.g., `count_int`, `buffer_ptr`)
5. **ALWAYS rename variables** - even partial understanding is better than default names
6. **Use descriptive partial names** like `some_financial`, `some_weapon`, `some_counter` when uncertain
7. **Add question marks** for uncertain identifications (e.g., `player_health?`, `mission_timer?`)

### **Reused Variable Naming**
- **Format**: `primary_purpose_or_secondary_purpose`
- **Examples**: 
  - `file_handle_or_error_code`
  - `loop_counter_or_array_index`
  - `temp_string_or_path_buffer`
  - `memory_size_or_bytes_remaining`

### **Specific Variable Types**

#### **Loop Variables**
- `loop_counter` - Simple incrementing counter
- `array_index` - Array traversal index
- `string_pos` - String position/character index
- `bit_position` - Bit manipulation position
- `retry_count` - Retry attempt counter

#### **Pointers & Buffers**
- `buffer_ptr` - Generic buffer pointer
- `string_ptr` - String pointer
- `current_pos` - Current position in buffer
- `end_ptr` - End of buffer/string
- `temp_buffer` - Temporary buffer
- `source_ptr` / `dest_ptr` - Source and destination pointers

#### **Size & Length Variables**
- `buffer_size` - Buffer size in bytes
- `string_length` - String length
- `bytes_remaining` - Remaining bytes to process
- `chars_to_copy` - Number of characters to copy
- `allocation_size` - Memory allocation size

#### **Status & Flags**
- `success_flag` - Boolean success indicator
- `error_occurred` - Error flag
- `found_match` - Search result flag
- `is_initialized` - Initialization state
- `operation_complete` - Completion status

#### **File & Path Variables**
- `file_path` - File path string
- `executable_name` - Executable filename
- `directory_path` - Directory path
- `file_handle` - File handle/descriptor
- `path_separator` - Path separator character

#### **Memory & Allocation**
- `allocated_memory` - Allocated memory pointer
- `memory_block` - Memory block pointer
- `heap_ptr` - Heap pointer
- `stack_ptr` - Stack pointer
- `overlay_segment` - Overlay memory segment

## 🚨 **CRITICAL ANALYSIS INSIGHTS**

### **Data vs Code Confusion**
- **Weird code patterns** may indicate **data accidentally flagged as code**
- **Look for**: Rare instructions, repeated identical instructions doing nothing logical
- **Action**: Re-examine as data structures, not executable code
- **Common signs**: Nonsensical instruction sequences, impossible jumps, invalid opcodes

### **Global Variable Priority (C Code)**
- **Global variables are CRITICAL** in C programs - they maintain program state
- **ALWAYS rename globals** with descriptive purposes immediately  
- **Global scope = game state** - these variables drive core functionality
- **Examples**: `player_stats`, `current_mission_data`, `game_world_state`

### **Uncertainty Handling**
- **Use question marks** for uncertain but likely identifications (`mission_timer?`)
- **Partial naming** is better than no naming (`some_financial` vs `DAT_1234`)  
- **Build context progressively** - partial names become clear as more code is analyzed
- **Ask for game context** when mechanisms are unclear - user has gameplay experience

## 💬 **COMMENT GUIDELINES**

### **When to Add Comments**
1. **Complex algorithms** - Any non-trivial logic
2. **Magic numbers** - Explain significance of constants
3. **DOS interrupts** - Explain what DOS call does
4. **Memory layouts** - Explain data structure organization
5. **Error handling** - Explain error conditions and recovery
6. **Business logic** - Explain game-specific functionality
7. **Optimizations** - Explain performance tricks
8. **Workarounds** - Explain why code is structured unusually
9. **Data vs code boundaries** - Mark where data was misidentified as code
10. **Global variable purposes** - Critical for understanding program state

### **Comment Format**
```c
// MAIN PURPOSE: Brief description of what this code does
// DETAILS: More detailed explanation if needed
// PARAMETERS: What parameters mean
// RETURNS: What the function returns
// SIDE EFFECTS: Any global state changes
// NOTES: Important implementation details
```

### **Specific Comment Types**

#### **Function Headers**
```c
// MAIN PURPOSE: Launches modal executable via table lookup
// DETAILS: Resolves executable path, sets up environment, calls DOS exec
// PARAMETERS: menu_choice - character from main menu ('g' for game, 'c' for code, etc.)
// RETURNS: 0 on success, error code on failure
// SIDE EFFECTS: Changes program state, launches external process
// NOTES: Uses PATH environment variable for executable resolution
```

#### **Complex Logic**
```c
// Parse command line arguments with quote handling
// Supports both single and double quotes with escape sequences
// Handles backslash escaping for embedded quotes
```

#### **DOS Interrupts**
```c
// DOS INT 21h AH=4Bh - Execute program
// AL=0: Load and execute program
// DS:DX = ASCIIZ program name
// ES:BX = Parameter block
```

#### **Memory Management**
```c
// Allocate memory for overlay with overflow protection
// Checks available memory before allocation
// Marks memory block as used in allocation table
```

#### **Error Handling**
```c
// Handle file not found error
// Display user-friendly error message
// Cleanup allocated resources before returning
```

## 🏷️ **LABEL NAMING CONVENTIONS**

### **Loop Labels**
- `loop_over_arguments`
- `loop_over_environment_vars`
- `loop_over_path_components`
- `loop_over_executables`
- `loop_until_found`

### **State Labels**
- `parsing_quotes`
- `handling_escapes`
- `processing_arguments`
- `cleanup_and_exit`
- `error_recovery`

### **Conditional Labels**
- `if_file_exists`
- `if_memory_available`
- `if_error_occurred`
- `if_initialization_complete`

## 🎯 **PRIORITY SYSTEM**

### **High Priority Functions** (Rename everything + Structure Hunt)
1. **GLOBAL VARIABLES** - **IMMEDIATE PRIORITY** - These define game state
2. **Core game logic** - main_menu_loop, launch functions, state management
3. **Memory management** - malloc, free, overlay functions
4. **File operations** - file launching, path resolution, save/load operations
5. **Error handling** - error display, cleanup
6. **Structure-heavy functions** - Any function with consistent offset patterns

### **Medium Priority Functions** (Rename key variables)
1. **String manipulation** - strcpy, strcat, strlen
2. **System initialization** - runtime setup, signal handlers
3. **Command line parsing** - argument processing

### **Low Priority Functions** (Add comments only)
1. **Simple thunks** - External function wrappers
2. **Trivial utilities** - Simple getters/setters

## 📊 **PROGRESS TRACKING**

### **Completion Checklist**
- [ ] **ALL GLOBAL VARIABLES RENAMED** - **CRITICAL PRIORITY**
- [ ] **Questionable identifications marked with ?**
- [ ] **Partial understanding captured in names** (some_weapon, some_counter)
- [ ] All parameters renamed with descriptive names
- [ ] All local variables renamed with purpose-clear names
- [ ] All loops have clear iteration variable names
- [ ] All pointers have clear target type names
- [ ] All buffers have clear size and purpose names
- [ ] All flags have clear boolean meaning names
- [ ] **Data vs code boundaries identified**
- [ ] **Structure patterns identified and documented**
- [ ] **Structure member access patterns mapped**
- [ ] **Data structure definitions created**
- [ ] Function purpose comment added
- [ ] Complex logic commented
- [ ] DOS interrupts documented
- [ ] Magic numbers explained
- [ ] Error handling documented
- [ ] **Save/load operations documented**

### **Quality Metrics**
- **Variable clarity**: Can purpose be understood from name alone?
- **Comment value**: Does comment explain something non-obvious?
- **Consistency**: Are similar concepts named similarly?
- **Completeness**: Are all non-trivial elements documented?

## 🏗️ **STRUCTURE IDENTIFICATION & DEFINITION**

### **String Arrays and Pointer Patterns**

**CRITICAL PATTERN**: When you find a bunch of C strings on a certain topic (e.g. agent names, location names, messages), there will be some structure to point to them:

1. **As part of a struct** - Structure members that are `char*` pointers
2. **Array of pointers** - Very common pattern: `char* string_array[]`

**Recognition Signs**: The data in pointer arrays will seem repetitive because it's referencing a bunch of adjacent memory addresses. Look for:
- Sequences of 4-byte values (32-bit pointers) that are close to each other
- Memory addresses that point to string data
- Patterns like: `0x1234, 0x1245, 0x1267, 0x1289` (adjacent string addresses)

**Example Pattern**:
```c
// DATA SECTION: Looks like repetitive 4-byte values
DAT_1000 = 0x2340;  // Points to "Anna"
DAT_1004 = 0x2345;  // Points to "Maria" 
DAT_1008 = 0x234b;  // Points to "Elena"
DAT_100c = 0x2351;  // Points to "Svetlana"

// ACTUAL STRUCTURE: Array of string pointers
char* female_agent_names[] = {
    "Anna",      // at 0x2340
    "Maria",     // at 0x2345
    "Elena",     // at 0x234b
    "Svetlana"   // at 0x2351
};
```

### **Recognizing Structures in Decompiled Code**

#### **Key Patterns That Indicate Structures:**

1. **Array Access with Fixed Offsets:**
   ```c
   // STRUCTURE PATTERN: Array of structures with consistent member access
   *(int *)(base_ptr + index * 0x20 + 0x4)    // .field_at_offset_4
   *(char *)(base_ptr + index * 0x20 + 0x8)   // .field_at_offset_8
   *(short *)(base_ptr + index * 0x20 + 0x10) // .field_at_offset_16
   // This suggests: struct[32_bytes] with int at +4, char at +8, short at +16
   ```

2. **Consistent Pointer Arithmetic:**
   ```c
   // STRUCTURE PATTERN: Single structure member access
   *(int *)(player_ptr + 0x14)     // player.health
   *(int *)(player_ptr + 0x18)     // player.mana
   *(char *)(player_ptr + 0x1c)    // player.level
   ```

3. **Loop-Based Structure Iteration:**
   ```c
   // STRUCTURE PATTERN: Iterating through array of structures
   for (i = 0; i < count; i++) {
       current_item = base_ptr + i * 0x30;  // 48-byte structures
       process_item(current_item);
   }
   ```

4. **Parameter Block Patterns:**
   ```c
   // STRUCTURE PATTERN: Function call parameter blocks
   param_block[0] = value1;    // .param1
   param_block[1] = value2;    // .param2
   param_block[2] = value3;    // .param3
   function_call(param_block);
   ```

### **Structure Definition Guidelines**

#### **Naming Conventions:**
- **Structure names**: `PascalCase` (e.g., `PlayerState`, `MissionData`, `ItemInfo`)
- **Member names**: `snake_case` (e.g., `health_points`, `mission_id`, `item_count`)
- **Array indicators**: Include size in name (e.g., `inventory_items[16]`, `skill_levels[4]`)

#### **Structure Documentation Format:**
```c
// STRUCTURE: PlayerState (Size: 64 bytes, 0x40)
// PURPOSE: Maintains complete player character state
// USAGE: Global player data, save/load operations
struct PlayerState {
    char player_name[16];        // +0x00: Player name (null-terminated)
    int health_points;           // +0x10: Current health (0-100)
    int max_health;              // +0x14: Maximum health capacity
    int skill_combat;            // +0x18: Combat skill level (0-10)
    int skill_stealth;           // +0x1C: Stealth skill level (0-10)
    int skill_electronics;       // +0x20: Electronics skill level (0-10)
    int skill_driving;           // +0x24: Driving skill level (0-10)
    int reputation;              // +0x28: Reputation points
    int current_mission_id;      // +0x2C: Active mission ID (-1 if none)
    int equipment_mask;          // +0x30: Bit mask of owned equipment
    int location_x;              // +0x34: Current X coordinate
    int location_y;              // +0x38: Current Y coordinate
    int reserved[1];             // +0x3C: Reserved/padding
};
```

### **Common Game Structure Patterns**

#### **1. Player/Character Structures:**
```c
struct Player {
    char name[32];              // Character name
    int attributes[6];          // Strength, dex, int, etc.
    int skills[8];              // Various skill levels
    int inventory[16];          // Item IDs in inventory
    int location_id;            // Current location
    int state_flags;            // Bit flags for various states
};
```

#### **2. Mission/Quest Structures:**
```c
struct Mission {
    int mission_id;             // Unique mission identifier
    char title[64];             // Mission title/name
    char description[256];      // Mission description
    int difficulty_level;       // 1-10 difficulty rating
    int time_limit;             // Time limit in game hours
    int objectives[8];          // Objective IDs to complete
    int rewards[4];             // Reward item IDs
    int status;                 // 0=available, 1=active, 2=complete
};
```

#### **3. Inventory/Item Structures:**
```c
struct Item {
    int item_id;                // Unique item identifier
    char name[32];              // Item display name
    int item_type;              // Category (weapon, tool, etc.)
    int value;                  // Monetary value
    int durability;             // Current durability
    int max_durability;         // Maximum durability
    int special_flags;          // Special properties bit mask
};
```

#### **4. Save Game Structures:**
```c
struct SaveGame {
    char signature[4];          // File format signature "SAV1"
    int version;                // Save file version number
    int checksum;               // Data integrity checksum
    struct PlayerState player;  // Player character data
    struct Mission missions[32]; // Mission status array
    struct Item inventory[64];   // Player inventory
    int global_flags[32];       // World state flags
    int game_time;              // Elapsed game time
};
```

### **Structure Identification Process**

#### **Step 1: Pattern Recognition**
1. **Look for repeated offset patterns** in memory accesses
2. **Identify consistent structure sizes** (multiples in loops)
3. **Find parameter passing patterns** that suggest structured data
4. **Observe related data groupings** that are accessed together

#### **Step 2: Size Calculation**
```c
// TECHNIQUE: Calculate structure size from array access
// If you see: base_ptr + index * 0x48
// Then each structure is 0x48 (72) bytes
```

#### **Step 3: Member Identification**
```c
// TECHNIQUE: Map offsets to member types
// +0x00: First member (often ID or size)
// +0x04: Second member 
// +0x08: Third member
// Look for consistent access patterns across multiple instances
```

#### **Step 4: Type Deduction**
- **4-byte accesses** → `int`, `float`, `pointer`
- **2-byte accesses** → `short`, `word`
- **1-byte accesses** → `char`, `byte`, `bool`
- **String patterns** → `char array[N]`
- **Zero-checks** → Often indicate counts or flags

### **Variable Naming for Structures**

#### **Structure Member Access:**
```c
// GOOD: Clear structure and member identification
player_state_ptr->health_points
mission_data[mission_index].time_limit
inventory_items[slot_index].item_id

// AVOID: Generic pointer arithmetic
*(int *)(ptr + 0x14)
data[i * 0x30 + 0x8]
```

#### **Structure Array Variables:**
```c
// NAMING PATTERN: type_array_purpose
PlayerState player_characters[MAX_PLAYERS];
Mission available_missions[32];
Item shop_inventory[64];
SaveGame save_slot_data[8];
```

#### **Structure Pointer Variables:**
```c
// NAMING PATTERN: purpose_ptr or current_type
PlayerState *current_player_ptr;
Mission *selected_mission_ptr;
Item *equipped_weapon_ptr;
SaveGame *active_save_ptr;
```

## 🔍 **REVERSE ENGINEERING INSIGHTS**

### **Common Patterns to Document**
1. **DOS executable patterns** - How programs are launched
2. **Memory overlay patterns** - How overlays are managed
3. **Error propagation patterns** - How errors flow through system
4. **String handling patterns** - How strings are processed
5. **Path resolution patterns** - How files are found
6. **Structure array patterns** - How game data is organized
7. **Save/load patterns** - How persistent data is managed

### **Historical Context Comments**
- **DOS limitations** - Why certain workarounds exist
- **Memory constraints** - Why overlay system is needed
- **16-bit specifics** - Why certain data types are used
- **MicroProse conventions** - Company-specific patterns

## 🚀 **IMPLEMENTATION STRATEGY**

### **Phase 1: Core Functions + Structure Hunt**
1. main_menu_loop
2. launch_generic_executable  
3. launch_code_breaking_game
4. find_executable_in_path
5. prepare_exec_environment
6. dos_exec_wrapper
7. **Identify all structure patterns in core functions**

### **Phase 2: Support Functions + Data Structures**
1. Memory management functions
2. String manipulation functions
3. Error handling functions
4. System initialization functions
5. **Save/load operations and file I/O**
6. **Define discovered data structures**

### **Phase 3: Utility Functions + State Management**
1. Command line parsing
2. Environment parsing
3. Signal handling
4. Cleanup functions
5. **Inter-module state passing mechanisms**
6. **Game state persistence patterns**

This systematic approach ensures comprehensive documentation while maintaining focus on the most critical reverse engineering insights. 