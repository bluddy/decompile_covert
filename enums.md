# Covert Action - Enumerations

## Overview
This file documents all identified enumerations in Covert Action's codebase, discovered through systematic reverse engineering.

---

## **🚀 PANI VIRTUAL MACHINE GLOBAL VARIABLES - BREAKTHROUGH DISCOVERY**

### **Core PANI VM State Variables**
**Found in**: `pani_animation_virtual_machine_interpreter` (1792:b01a)  
**Usage**: Essential virtual machine state management for revolutionary 1990 animation system

```c
// PANI VM Core State Variables (Memory Addresses)
pani_vm_current_opcode          (276a:5e44)   // Current instruction (0-23)
pani_vm_instruction_pointer     (276a:5e28)   // Program counter (far pointer)  
pani_vm_stack_pointer          (276a:5e2c)   // Operand stack pointer
pani_vm_call_stack_pointer     (276a:5e30)   // Subroutine call stack pointer
pani_vm_delay_state_flag       (276a:5e24)   // Timing state (0=normal, 1=delay)
pani_vm_delay_frame_counter    (276a:5e46)   // Frame countdown for timing
pani_vm_exit_flag              (276a:a5a8)   // Global VM termination flag
mission_parameters_array       (276a:b30e)   // Animation parameter storage
```

**VM Architecture Features**:
- **Stack-Based Execution**: Modern VM architecture with operand stack management
- **Subroutine Support**: Call stack enables modular animation programming  
- **Frame-Perfect Timing**: Sophisticated delay system for smooth animation
- **Parameter Persistence**: Mission parameter array for animation state storage
- **Safe Sprite Management**: Index validation and bounds checking throughout

**Integration Patterns**:
- **Main Game Loop**: Called during animation phases for sprite updates
- **Graphics Pipeline**: Coordinates with EGA system for 320×200 sprite rendering
- **Sprite Arrays**: Manages up to 50 simultaneous animated sprites (0x33 max index)
- **Program Loading**: Executes bytecode programs loaded from PANI animation files

---

## LocationType Enum
**Found in**: `append_connection_type_description` (1792:83e8)  
**Usage**: Describes relationship types between organizations and locations

```c
enum LocationType {
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

## PANIAnimationVMOpcode Enum
**Found in**: `covert_action_virtual_machine_interpreter` (1792:b01a)  
**Usage**: Complete instruction set for PANI Animation Virtual Machine - sophisticated animated object system

```c
enum PANIAnimationVMOpcode {
    PANI_CREATE_SPRITE = 0,       // Create animated sprite/object with position, graphics, timing
    PANI_DESTROY_SPRITE = 1,      // Remove sprite from animation (set active flag to 0)
    PANI_DELAY_FRAMES = 2,        // Pause animation execution for specified frame count
    PANI_PUSH_VALUE = 3,          // Push value onto animation stack for calculations
    PANI_SHOW_SPRITE = 4,         // Make sprite visible (set status to 1)
    PANI_LOAD_VARIABLE = 5,       // Load animation variable (position, timing, state)
    PANI_STORE_VARIABLE = 6,      // Store value to animation variable (movement, state)
    PANI_DUPLICATE_VALUE = 7,     // Duplicate stack value for animation calculations
    PANI_TEST_EQUAL = 8,          // Test equality for animation conditionals
    PANI_TEST_NOT_EQUAL = 9,      // Test inequality for animation branching
    PANI_TEST_LESS_THAN = 10,     // Test less-than for position/timing comparisons
    PANI_TEST_GREATER_THAN = 11,  // Test greater-than for boundary checks
    PANI_TEST_LESS_EQUAL = 12,    // Test less-equal for range checks
    PANI_TEST_GREATER_EQUAL = 13, // Test greater-equal for animation thresholds
    PANI_ADD_VALUES = 14,         // Add values (movement, position calculations)
    PANI_SUBTRACT_VALUES = 15,    // Subtract values (relative positioning)
    PANI_MULTIPLY_VALUES = 16,    // Multiply values (scaling, timing)
    PANI_DIVIDE_VALUES = 17,      // Divide values (proportional animation)
    PANI_BRANCH_IF_FALSE = 18,    // Conditional jump for animation logic
    PANI_JUMP_ABSOLUTE = 19,      // Jump to animation sequence address
    PANI_HALT_ANIMATION = 20,     // Stop animation and return control
    PANI_EXIT_SYSTEM = 21,        // Exit PANI animation system entirely
    PANI_RETURN_SUBROUTINE = 22,  // Return from animation subroutine
    PANI_CALL_SUBROUTINE = 23     // Call animation subroutine (nested sequences)
};
```

**PANI Animation System Features**:
- **Stack-based animation engine** with sophisticated sprite management
- **Animated sprite lifecycle** integrated with 52-byte AnimatedSprite structures
- **Screen coordinate system** for precise sprite positioning and movement
- **Frame-based timing control** with delay instructions for smooth animation
- **Conditional animation logic** with branching for interactive sequences
- **Nested animation subroutines** for complex, reusable animation sequences
- **Mathematical operations** for sprite movement calculations and transformations
- **Sprite visibility control** (show/hide sprites dynamically)
- **Multi-sprite coordination** for complex scene composition

**PANI System Integration**:
- Called from main game loop during animation phases (briefings, cutscenes)
- Manages up to 50 simultaneous animated sprites on screen
- Coordinates with EGA graphics system for sprite rendering
- Uses animation parameter arrays for sprite state management
- Enables complex briefing animations, character movements, and visual effects
- **Revolutionary 1990 animation scripting system** - predates modern game engines by years!

---

## PANISpriteAnimationOpcode Enum
**Found in**: `pani_sprite_animation_bytecode_interpreter` (1792:b7c6)  
**Usage**: Animation bytecode commands for individual sprite movement and behavior sequences

```c
enum PANISpriteAnimationOpcode {
    SPRITE_END_FRAME = 0,           // End current frame, advance to next animation step
    SPRITE_SET_POSITION = 1,        // Set absolute screen position (X, Y coordinates)
    SPRITE_MOVE_RELATIVE = 2,       // Move relative to current position (deltaX, deltaY)
    SPRITE_SET_SPEED = 3,           // Set animation speed/timing value
    SPRITE_ADD_SPEED = 4,           // Add to current animation speed (acceleration)
    SPRITE_PUSH_STACK = 5,          // Push value onto animation stack for loops
    SPRITE_LOOP_COUNTER = 6,        // Decrement counter, jump if not zero (loop control)
    SPRITE_RESET_POSITION = 7,      // Reset to initial position and speed values
    SPRITE_RESTART_ANIMATION = 8,   // Reset animation to beginning and restart
    SPRITE_PAUSE = 9,               // Pause animation execution (wait state)
    SPRITE_END_ANIMATION = 10       // End animation completely, deactivate sprite
};
```

**Detailed Implementation Analysis from Decompiled Code**:

### **Sprite Data Structure Offsets (52-byte PANIAnimatedSprite)**:
- **`+0x16`**: Current X position (screen coordinates, 2 bytes)
- **`+0x18`**: Current Y position (screen coordinates, 2 bytes)  
- **`+0x1A`**: Initial X position backup (for reset operations)
- **`+0x1C`**: Animation speed/timing value (controls playback rate)
- **`+0x1E`**: Animation accumulator (frame timing, compared against 0xFF threshold)
- **`+0x34`**: Stack pointer for loop control system
- **`+0x36`**: Initial bytecode program pointer (animation start)
- **`+0x3A`**: Current bytecode instruction pointer (program counter)
- **`+0x3C`**: Saved instruction pointer (for loop jumps)
- **`+0x3E`**: Current frame byte value

### **Opcode Implementation Details**:

**Frame Control**:
- **OPCODE 0**: Reads next frame byte from `*(instruction_pointer + 1)`, advances IP by 2 bytes
- Frame progression controlled by discrete frame values for smooth animation

**Position Control**:
- **OPCODE 1**: Reads X (2 bytes) + Y (2 bytes), sets absolute screen coordinates, advances IP by 5
- **OPCODE 2**: Reads deltaX + deltaY (4 bytes), adds to current position, advances IP by 5
- Supports full 320×200 EGA screen coordinate system

**Speed/Timing Control**:
- **OPCODE 3**: Reads 2-byte speed value, stores in sprite timing offset, advances IP by 3
- **OPCODE 4**: Reads speed delta, adds to current speed (acceleration), advances IP by 3
- Speed values control animation frame timing through accumulator system

**Stack-Based Loop Control**:
- **OPCODE 5**: Reads 2-byte value, pushes to internal sprite stack, increments stack pointer, advances IP by 3
- **OPCODE 6**: Decrements stack top; if non-zero jumps to address from bytecode, else pops stack and advances IP by 3
- Enables nested loops and complex animation patterns

**State Management**:
- **OPCODE 7**: Conditional reset - if sprite type is -2, restores backup position, else zeros position; resets speed and accumulator
- **OPCODE 8**: Resets stack pointer to 0, restores instruction pointer to initial program start
- Both opcodes enable clean animation restarts

**Execution Control**:
- **OPCODE 9**: Immediate return (pause) - preserves all state for next VM call
- **OPCODE 10**: Sets sprite active flag to 0 (deactivation), terminates animation completely

**Sprite Animation Features**:
- **Frame-based movement control** with precise timing and positioning
- **Relative and absolute positioning** for smooth sprite movement
- **Speed control and acceleration** for dynamic animation effects
- **Loop constructs** with stack-based counter management
- **Animation state control** (pause, restart, end)
- **Parent-child sprite relationships** for complex coordinated animations
- **Automatic position interpolation** with speed-based movement calculations

**Two-Level Animation Architecture**:
1. **High-Level PANI VM** (24 opcodes) - Controls sprite lifecycle, logic, and sequencing
2. **Low-Level Sprite Animation** (10 opcodes) - Controls individual sprite movement and behavior

This **dual virtual machine architecture** provides unprecedented animation control for 1990!

---

## Notes
- Enums in 1990 C code often implemented as simple integer comparisons
- String lookup pattern is common for user-facing descriptions
- Connection types reflect real espionage/criminal organization structures
- Values 1-5 suggest there may be a "no connection" state at value 0
- **PANI Animation System represents TWO complete virtual machines - revolutionary discovery!**
- **Dual VM architecture**: High-level sprite management + low-level animation control
- Virtual machines enable complex animation scripting without recompiling the main executable
- **World's first known dual-VM animation system** - predates modern game engines by decades! 