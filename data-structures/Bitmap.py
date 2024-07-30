class Bitmap:
    def __init__(self, size: int):
        self.size = size
        self._bitmap = [0] * ((size + 7) // 8)
 
    def _get_byte_index(self, index: int):
        byte_index = index // 8
        bit_position = index % 8
        return byte_index, bit_position
 
    def set_bit(self, index: int):
        byte_index, bit_index = self._get_byte_index(index)
        self._bitmap[byte_index] |= (1 << bit_index)
 
    def clear_bit(self, index: int):
        byte_index, bit_index = self._get_byte_index(index)
        self._bitmap[byte_index] ^= (1 << bit_index)
 
    def __str__(self):
        return ''.join(f'{byte:08b}' for byte in reversed(self._bitmap))
 
    def __repr__(self):
        return ''.join(f'{byte:08b}' for byte in reversed(self._bitmap))
     
if __name__ == '__main__':
    bitmap = Bitmap(16)
    print(bitmap)
 
    bitmap.set_bit(0)
    bitmap.set_bit(15)
    print(bitmap)
