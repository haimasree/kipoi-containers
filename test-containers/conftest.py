from pathlib import Path
import json


def pytest_addoption(parser):
    """ attaches optional cmd-line args to the pytest machinery """
    parser.addoption("--model", action="append", default=[], help="model name")
    parser.addoption(
        "--all",
        action="store_true",
        help="run all model groups with one representative model",
    )


def pytest_generate_tests(metafunc):
    with open(
        Path.cwd() / "test-containers" / "model-group-to-image-name.json", "r"
    ) as infile:
        metafunc.cls.model_group_to_image_dict = json.load(infile)

    if metafunc.config.getoption("all"):
        metafunc.cls.list_of_models = [
            "DeepCpG_DNA/Hou2016_HepG2_dna",
            "CpGenie/A549_ENCSR000DDI",
            "Divergent421",
            "Basenji",
            "Basset",
            "HAL",
            "DeepSEA/variantEffects",
            "Optimus_5Prime",
            "labranchor",
            "CleTimer/customBP",
            "SiSp",
            "FactorNet/FOXA2/onePeak_Unique35_DGF",
            "MaxEntScan/5prime",
            "pwm_HOCOMOCO/human/AHR",
            "DeepBind/Arabidopsis_thaliana/RBP/D00283.001_RNAcompete_At_0284",
            "lsgkm-SVM/Chip/OpenChrom/Cmyc/K562",
            "rbp_eclip/AARS",
            "MPRA-DragoNN/DeepFactorizedModel",
            "extended_coda",
            "MMSplice/deltaLogitPSI",
            "MMSplice/mtsplice",
            "DeepMEL",
            "Framepool",
            "KipoiSplice/4cons",
            "deepTarget",
            "AttentiveChrome/E003",
            "BPNet-OSKN",
        ]
    else:
        model_from_cmd_line = metafunc.config.getoption("model")
        if model_from_cmd_line and hasattr(metafunc.cls, "model_name"):
            metafunc.cls.model_name = model_from_cmd_line[0]