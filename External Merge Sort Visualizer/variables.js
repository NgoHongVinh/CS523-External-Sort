// Max allowed number of relations per page (past this number relations get impossible to see)
const MAX_RECORDS_PER_PAGE = 50;
// Sorting algorithms
var algorithm_type = {
	two_way: 0,
	k_way: 1,
	replacement_selection: 2,
}

const LOG_DEBUG = false;

// Algorithm type
var selected_algorithm_type = 1;

// Input values
var num_of_frames_in_buffer = -1;
var num_of_records_per_page = -1;
var num_of_records_of_file = -1;
var num_of_pages_of_file = -1;

var animation_velocities = {
	speed_3_00: 12,	// 3x
	speed_2_50: 10.5,
	speed_2_00: 9,	// 2x
	speed_1_75: 8,
	speed_1_50: 7,
	speed_1_25: 6,
	speed_1_00: 5,	// 1x
	speed_0_75: 4,
	speed_0_50: 3,
	speed_0_25: 2,
}
// Current animation speed
var selected_animation_speed_multiplier;

// ANIMATION
var pause_in_between_animation_phases;
var animation_is_playing = false;
var animate_forward_step = true;

// Other variables
var time = 0;
const ANIMATION_STEP_MULTIPLIER = 100; // NOTE: Don't change this, change animation_speed instead (this is also the minimum time in ms hte user needs to wait to move forwards / backwards with steps)

var STEP_DURATION;

// Other input variables ------------------------

var enable_focus_on_element = true;
var enable_algorithm_lines_highlighting = true;
var frames_run_number_associations_visible = true;

function set_enable_focus_on_element(value) {
	enable_focus_on_element = value;
}

function set_enable_algorithm_lines_highlighting(value) {
	enable_algorithm_lines_highlighting = value;
	if (enable_algorithm_lines_highlighting) {
		// Set code lines to correct code lines
		if (current_phase >= 0 && current_phase < animation.length) {
			let phase_info = animation[current_phase + 1].phase_info;
			move_code_line_to(phase_info.code_line, phase_info.code_line_offset);
		}
	} else {
		// Hide code line
		move_code_line_to([-1]);
	}
}

function set_enable_frames_run_number_associations_visible(value) {
	frames_run_number_associations_visible = value;
	toggle_frames_run_number_associations(value);
}

