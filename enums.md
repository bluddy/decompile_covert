# Covert Action - Enumerations

## Overview
This file documents all identified enumerations in Covert Action's codebase, discovered through systematic reverse engineering.

---

## ConnectionType Enum
**Found in**: `append_connection_type_description` (1792:83e8)  
**Usage**: Describes relationship types between organizations and locations

```c
enum ConnectionType {
    HIDEOUT = 1,        // "hideout" - Criminal hideout location
    AGENT = 2,          // "agent" - Agent or contact person  
    SAFEHOUSE = 3,      // "safehouse" - Safe meeting location
    ACTIVE_CELL = 4,    // "active cel" - Active criminal cell
    OFFICE = 5          // "office" - Official/business front
};
```

**Function Implementation**:
- Converts connection strength values (1-5) into descriptive text
- Used by intelligence discovery engine for generating reports
- Appends appropriate text to global string buffer for display
- Critical for player understanding of criminal network structure

**String Constants**:
- `s_connection_hideout` (276a:3fe4): "hideout"
- `s_connection_agent` (276a:3fed): "agent" 
- `s_connection_safehouse` (276a:3ff4): "safehouse"
- `s_connection_active_cell` (276a:3fff): "active cel"
- `s_connection_office` (276a:400b): "office"

---

## Notes
- Enums in 1990 C code often implemented as simple integer comparisons
- String lookup pattern is common for user-facing descriptions
- Connection types reflect real espionage/criminal organization structures
- Values 1-5 suggest there may be a "no connection" state at value 0 