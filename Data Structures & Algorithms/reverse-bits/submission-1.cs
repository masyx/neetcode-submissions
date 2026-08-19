public class Solution {
    public uint ReverseBits(uint n) {
        uint result = 0;
        uint mask = 1;
        for(int i = 0; i < 32; i++)
        {
            var bit = (n >> i) & mask;
            result |= bit << (31 - i); 
        }
        return result;
    }
}
