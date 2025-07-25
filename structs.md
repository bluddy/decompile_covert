# Covert Action - Data Structures

## Overview
This file documents all identified data structures in Covert Action's codebase, discovered through systematic reverse engineering.

---

## Person Structure
**Size**: 16 bytes (0x10)  
**Found in**: `intelligence_discovery_and_clue_generation_engine` (1792:524c)  
**Base Address Pattern**: `person_index * 0x10 + base_offset`

```c
struct Person {
    int organization_id;         // +0x188: Organization ID (0-15)
    int person_attributes;       // +0x18A: Unique ID/portrait ID  
    int location_id;             // +0x18C: Location ID (0-15)
    uint intelligence_flags;     // +0x18E: Intelligence discovery flags
    uint case_involvement;       // +0x190: Case involvement bitmask
    uint role_flags;            // +0x192: Current role flags
    uint additional_data;       // +0x194: Status/score/additional attributes
    int status;                 // +0x196: Character status (active/arrested/hiding/turned)
};
```

**Usage**:
- Core character database for all NPCs and agents
- Tracks relationships between people, organizations, and locations
- Manages progressive intelligence discovery through bit flags
- Integrates with chronology events and case progression

---

## ChronologyEvent Structure  
**Size**: 14 bytes (0xe)  
**Found in**: `intelligence_discovery_and_clue_generation_engine` (1792:524c)  
**Base Address Pattern**: `event_index * 0xe + chronology_base`

```c
struct ChronologyEvent {
    int event_id;              // +0x84BC: Crime ID or message (-1 for message)
    uint discovery_flags;      // +0x84BE: What player has discovered (bit flags)
    char person1;             // +0x84C2: First character involved
    char person2;             // +0x84C4: Second character involved  
    char location;            // +0x84C5: Location where event occurred
    // Additional fields up to 14 bytes total
};
```

**Usage**:
- Timeline management for case progression
- Links characters, locations, and events
- Tracks player's investigative progress
- Generates dynamic briefings and intelligence reports

---

## Organization Structure
**Size**: 36 bytes (0x24)  
**Found in**: `intelligence_discovery_and_clue_generation_engine` (1792:524c)  
**Base Address Pattern**: `org_id * 0x24 + org_data_base`

```c
struct Organization {
    uint coordinates;           // +0x00: Packed 4-bit X/Y coordinates
    uint power_level;          // +0x04: Organization strength/influence
    uint attributes;           // +0x08: Organization attributes/flags
    char name[24];            // +0x0C: Organization name (null-terminated)
    // Additional data up to 36 bytes total
};
```

**Usage**:
- Criminal organization database (16 total organizations)
- Geographic positioning with coordinate system
- Power/influence calculations for connection strength
- Name storage for intelligence reports and briefings

---

## PANIAnimatedSprite Structure
**Size**: 52 bytes (0x34)  
**Found in**: `initialize_game_object_structure_52_bytes` (1792:b4ea)  
**Base Address Pattern**: `sprite_index * 0x34 + base_offset_0x7d8`

### **Complete Structure Layout from Second Tier VM Analysis:**

```c
struct PANIAnimatedSprite {
    // Core sprite state
    uint active_flag;            // +0x00: Sprite active/visible flag (1 = active)
    uint animation_status;       // +0x02: Animation state (0 = hidden, 1 = visible)
    int sprite_type_id;          // +0x04: Sprite graphics ID or animation type (param - 1)
    
    // Position management
    uint screen_x;               // +0x06: Current X screen coordinate (0-319)
    uint screen_y;               // +0x08: Current Y screen coordinate (0-199)
    uint backup_x;               // +0x0A: Previous/backup X position for animation
    uint backup_y;               // +0x0C: Previous/backup Y position for animation
    
    // Animation timing and control
    uint animation_param;        // +0x0E: Animation-specific parameter (speed, frame, etc.)
    uint animation_param_copy;   // +0x10: Duplicate of animation parameter for state
    uint timing_flag;            // +0x12: Animation timing flag (0xFF for max timing)
    
    // Second tier VM state (from low-level bytecode interpreter)
    uint animation_counter;      // +0x28: Frame counter or animation state
    uint graphics_data_ref;      // +0x2A: Reference to sprite graphics data
    uint animation_sequence;     // +0x2C: Animation sequence or pattern ID
    uint graphics_data_copy;     // +0x2E: Copy of graphics reference
    uint global_animation_ref;   // +0x30: Reference to global animation parameters
    
    // Second tier VM execution state (detailed offsets)
    uint current_x;              // +0x16: Current X position (2 bytes) - VM coordinate system
    uint current_y;              // +0x18: Current Y position (2 bytes) - VM coordinate system
    uint initial_x;              // +0x1A: Initial X position backup (for reset operations)
    uint animation_speed;        // +0x1C: Animation speed/timing value (controls playback rate)
    uint frame_accumulator;      // +0x1E: Animation accumulator (frame timing, 0xFF threshold)
    
    // Bytecode execution state
    uint loop_stack_pointer;     // +0x34: Stack pointer for loop control system
    uint program_start;          // +0x36: Initial bytecode program pointer (animation start)
    uint instruction_pointer;    // +0x3A: Current bytecode instruction pointer (program counter)
    uint saved_instruction_ptr;  // +0x3C: Saved instruction pointer (for loop jumps)
    uint current_frame_byte;     // +0x3E: Current frame byte value
};
```

### **Second Tier VM Integration Details:**

**Memory Layout for Low-Level VM:**
- **Sprite Index Calculation**: `sprite_index * 0x34` (52-byte structures)
- **Base Address**: Sprite array base + calculated offset
- **Maximum Sprites**: 51 (0x33 max index)

**VM State Offsets (used by `pani_sprite_animation_bytecode_interpreter`):**
- **+0x16**: Current X position (screen coordinates, 2 bytes)
- **+0x18**: Current Y position (screen coordinates, 2 bytes)  
- **+0x1A**: Initial X position backup (for reset operations)
- **+0x1C**: Animation speed/timing value (controls playback rate)
- **+0x1E**: Animation accumulator (frame timing, compared against 0xFF threshold)
- **+0x34**: Stack pointer for loop control system
- **+0x36**: Initial bytecode program pointer (animation start)
- **+0x3A**: Current bytecode instruction pointer (program counter)
- **+0x3C**: Saved instruction pointer (for loop jumps)
- **+0x3E**: Current frame byte value

### **Second Tier VM Opcode Integration:**

**Bytecode Execution:**
- **Instruction Pointer**: Advances by opcode-specific byte counts
- **Position Updates**: Absolute (5 bytes) or relative (5 bytes) movement
- **Speed Control**: 2-byte values for speed/acceleration
- **Loop Management**: Stack-based counter system with nested support

**Animation Timing:**
- **Frame Accumulator**: Compared against 0xFF threshold for frame timing
- **Speed Values**: Control animation playback rate
- **Frame Bytes**: Discrete values for smooth progression

### **PANI Animation Usage:**
- **Sprite lifecycle management** for PANI animation sequences
- **Screen positioning system** with EGA coordinate mapping (320×200)
- **Animation state preservation** with backup coordinate system for smooth movement
- **Graphics integration** with sprite data references and rendering parameters
- **Frame-based animation** with timing controls and sequence management
- **Multi-sprite coordination** for complex briefing and cutscene animations
- **Dual VM architecture**: High-level VM manages sprites, low-level VM handles movement

### **Revolutionary 1990 Features:**
- **Stack-based loop control** predates modern scripting by years
- **Individual bytecode programs** per sprite
- **Speed modulation** and acceleration support
- **Nested animation sequences** with proper state management
- **Frame-perfect timing** with 0xFF accumulator threshold
- **Complete dual VM architecture** - world's first known in games

---

## GameConfiguration Structure
**Size**: 14+ bytes (7+ fields, 2 bytes each)  
**Found in**: `process_game_configuration_structure` (1792:ac84)  
**Base Address Pattern**: Pointer-based access with array indices [0] to [6]

```c
struct GameConfiguration {
    uint validation_field;       // [0]: Used for structure validation
    uint field_1;               // [1]: Unknown field  
    uint config_parameter;      // [2]: Main configuration parameter
    uint scaling_factor;        // [3]: Used in mathematical calculations with global variables
    uint coordinate_x;          // [4]: X coordinate (-1 = no change)
    uint coordinate_y;          // [5]: Y coordinate (-1 = no change)
    uint display_parameter;     // [6]: Display/graphics parameter (-1 = no change)
    // Possibly additional fields beyond index 6
};
```

**Usage**:
- Game initialization and configuration management
- Coordinate system setup for graphics/gameplay
- Conditional parameter setting (uses -1 as "no change" sentinel)
- Mathematical scaling calculations for game timing/difficulty
- Integration with graphics coordinate system
- Validation-based structure processing (field [0] must pass validation)

---

## Notes
- All structures use consistent offset patterns for array access
- Bit flag systems are extensively used for state management
- 16-bit DOS memory constraints influence structure sizes
- Cross-references between structures create complex relationship networks
- **PANIAnimatedSprite structure enables revolutionary 1990 animation system** with backup coordinate smoothing
- GameConfiguration structure uses -1 as sentinel values for optional parameters
- **PANI animation system predates modern game engine architecture by years** - complete sprite management with VM scripting 