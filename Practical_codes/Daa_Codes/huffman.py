import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char, self.freq = char, freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(frequencies):
    """Builds the Huffman tree and returns the root node."""
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left, right = heapq.heappop(heap), heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def get_codes(node, prefix="", codes=None):
    """Recursively generates binary codes for each character."""
    if codes is None: codes = {}
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        get_codes(node.left, prefix + "0", codes)
        get_codes(node.right, prefix + "1", codes)
    return codes

def decode(encoded_text, root):
    """Decodes a binary string back to text."""
    result, current = [], root
    for bit in encoded_text:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            result.append(current.char)
            current = root
    return "".join(result)

def main():
    print("=== Huffman Encoding ===")
    choice = input("1: Plain string text\n2: Frequencies (e.g., A:12, B:15)\nChoice (1/2): ").strip()

    if choice == '1':
        text = input("Enter text: ")
        if not text: return
        
        root = build_tree(Counter(text))
        codes = get_codes(root)
        encoded = "".join(codes[char] for char in text)
        
        print(f"\nEncoded Binary: {encoded}")
        print(f"Decoded Check: '{decode(encoded, root)}'")

    elif choice == '2':
        data = input("Enter frequencies (e.g., A:12, B:15, C:7, D:13, E:9): ")
        try:
            # Parses "A:12, B:15" into {'A': 12, 'B': 15} in one line
            freqs = {k.strip(): int(v) for k, v in (pair.split(':') for pair in data.split(','))}
            codes = get_codes(build_tree(freqs))
        except ValueError:
            print("Error: Invalid format.")
            return
    else:
        print("Invalid choice.")
        return

    # Shared output for both modes
    print("\nGenerated Huffman Codes:")
    for char, code in sorted(codes.items(), key=lambda x: len(x[1])):
        print(f"  '{char}': {code}")

if __name__ == "__main__":
    main()