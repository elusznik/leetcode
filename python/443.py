class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ptr = 0
        read_ptr = 0
        n = len(chars)
        while read_ptr < n:
            current_char = chars[read_ptr]
            count = 0
            group_end_ptr = read_ptr
            while group_end_ptr < n and chars[group_end_ptr] == current_char:
                group_end_ptr += 1
                count += 1
            chars[write_ptr] = current_char
            write_ptr += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1
            read_ptr = group_end_ptr
        del chars[write_ptr:]
        return len(chars)