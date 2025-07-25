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

## GameObject Structure
**Size**: 52 bytes (0x34)  
**Found in**: `initialize_game_object_structure_52_bytes` (1792:b4ea)  
**Base Address Pattern**: `object_index * 0x34 + base_offset_0x7d8`

```c
struct GameObject {
    uint active_flag;            // +0x00: Active/initialized flag (set to 1)
    uint status;                 // +0x02: Object status (initialized to 0)
    int object_id;               // +0x04: Object ID or type (param - 1)
    uint position_x;             // +0x06: X coordinate or parameter 4
    uint position_y;             // +0x08: Y coordinate or parameter 5  
    uint backup_x;               // +0x0A: Backup X (conditional copy from position_x)
    uint backup_y;               // +0x0C: Backup Y (conditional copy from position_y)
    uint parameter_6;            // +0x0E: Parameter 6 value
    uint parameter_6_copy;       // +0x10: Duplicate of parameter 6
    uint max_value_flag;         // +0x12: Set to 0xFF (max value indicator)
    // ... gap in analyzed offsets ...
    uint field_28;               // +0x28: Initialized to 0
    uint field_2A;               // +0x2A: Parameter 2 value
    uint field_2C;               // +0x2C: Parameter 7 value  
    uint field_2E;               // +0x2E: Copy of parameter 2
    uint global_reference;       // +0x30: Reference to global variable (276a:9e80)
    // Additional fields up to 52 bytes total
};
```

**Usage**:
- Game object initialization and management system
- Handles positioning with backup coordinate system
- Special case logic for object_id == -1 (triggers coordinate backup)
- Integrates with global game state management
- Supports parameter duplication for state preservation

---

## Notes
- All structures use consistent offset patterns for array access
- Bit flag systems are extensively used for state management
- 16-bit DOS memory constraints influence structure sizes
- Cross-references between structures create complex relationship networks
- GameObject structure shows sophisticated parameter management with backup systems 