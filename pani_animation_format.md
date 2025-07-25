# PANI Animation Format specification

**VM Architecture Features**:
- **Stack-Based Execution**: Modern VM architecture with operand stack management
- **Subroutine Support**: Call stack enables modular animation programming  
- **Frame-Perfect Timing**: Sophisticated delay system for smooth animation
- **Parameter Persistence**: Mission parameter array for animation state storage
- **Safe Sprite Management**: Index validation and bounds checking throughout
- Virtual machines enable complex animation scripting without recompiling the main executable

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

**Integration Patterns**:
- **Main Game Loop**: Called during animation phases for sprite updates
- **Graphics Pipeline**: Coordinates with EGA system for 320×200 sprite rendering
- **Sprite Arrays**: Manages up to 50 simultaneous animated sprites (0x33 max index)
- **Program Loading**: Executes bytecode programs loaded from PANI animation files


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