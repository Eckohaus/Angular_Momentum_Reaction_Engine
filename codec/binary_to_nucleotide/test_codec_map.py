# codec/binary_to_nucleotide/test_codec_map.py
import json
import os

def load_codec_map(path="codec_map.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_codec_structure(codec_map):
    codec = codec_map.get("codec", {})
    assert all(pair in codec for pair in ["00", "01", "10", "11"]), "Missing bit-pair mappings"
    for key, value in codec.items():
        assert "symbol" in value and len(value["symbol"]) == 1, f"Invalid symbol for {key}"
    print("✅ Codec structure validated.")

def translate(binary_str, codec_map):
    codec = codec_map["codec"]
    return "".join(codec.get(binary_str[i:i+2], {"symbol": "?"})["symbol"] for i in range(0, len(binary_str), 2))

def reverse_translate(nucleotide_str, codec_map):
    codec = codec_map["codec"]
    reverse = {v["symbol"]: k for k, v in codec.items()}
    return "".join(reverse.get(nuc, "??") for nuc in nucleotide_str)

def test_round_trip(codec_map):
    binary_input = "00101111"
    nucleotide_seq = translate(binary_input, codec_map)
    binary_output = reverse_translate(nucleotide_seq, codec_map)
    assert binary_input == binary_output, f"Round-trip failed: {binary_input} → {nucleotide_seq} → {binary_output}"
    print(f"🔁 Round-trip successful: {binary_input} → {nucleotide_seq} → {binary_output}")

if __name__ == "__main__":
    path = os.path.join(os.path.dirname(__file__), "codec_map.json")
    codec_map = load_codec_map(path)
    validate_codec_structure(codec_map)
    test_round_trip(codec_map)
