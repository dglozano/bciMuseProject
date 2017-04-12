import pickle

# TODO 01: add the path that are left
# TODO 02: analyze if it should be better to change to JSON format and add more data to each path

PATHS = {
    'eeg_raw': '/muse/egg',
    'eeg_quantization_level': '/muse/eeg/quantization',
    'eeg_dropped_samples': '/muse/eeg/dropped_samples',
    'acc': '/muse/acc',
    'acc_dropped_samples': '/muse/acc/dropped_samples',
    'abs_low_freqs': '/muse/elements/low_freqs_absolute',
    'abs_delta': '/muse/elements/delta_absolute',
    'abs_theta': '/muse/elements/theta_absolute',
    'abs_alpha': '/muse/elements/alpha_absolute',
    'abs_beta': '/muse/elements/beta_absolute',
    'abs_gamma': '/muse/elements/gamma_absolute',
    'ssc_delta': '/muse/elements/delta_session_score',
    'ssc_theta': '/muse/elements/theta_session_score',
    'ssc_alpha': '/muse/elements/alpha_session_score',
    'ssc_beta': '/muse/elements/bet_session_score',
    'ssc_gamma': '/muse/elements/gamma_session_score',
    'touching': '/muse/elements/touching_forehead',
    'horsesshoe': '/muse/elements/horseshoe',
    'is_good': '/muse/elements/is_good',
    'blink': '/muse/elements/blink',
    'jaw_clench': '/muse/elements/jaw_clench'
}

pickle.dump(PATHS, open("paths.p", "wb"))
