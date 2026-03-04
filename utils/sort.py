import os
import heapq
import struct
import tempfile
import argparse

DOUBLE_SIZE = 8 

def read_doubles(f, count):
    """
    Đọc một số lượng phần tử double từ file nhị phân.

    Parameters
    ----------
    f : file object
        File đã mở ở chế độ nhị phân ('rb').
    count : int
        Số lượng phần tử double (8 bytes) cần đọc.

    Returns
    -------
    list[float]
        Danh sách các số thực đọc được.
        Trả về list rỗng nếu không còn dữ liệu.
    """
    data = f.read(count * DOUBLE_SIZE)
    if not data:
        return []
    return list(struct.unpack("<" + "d" * (len(data) // DOUBLE_SIZE), data))


def write_doubles(f, arr):
    """
    Ghi danh sách số thực double vào file nhị phân (little-endian).
    """
    if not arr:
        return
    data = struct.pack("<" + "d" * len(arr), *arr)
    f.write(data)


def create_temp_file():
    """
    Tạo file tạm an toàn trên Windows (không giữ file handle).
    """
    fd, path = tempfile.mkstemp()
    os.close(fd)
    return path


def external_merge_sort(input_path, num_buffers=4, chunk_size=100000):
    """
    Thực hiện External Merge Sort trên file .bin chứa double 8 bytes.

    Parameters
    ----------
    input_path : str
        Đường dẫn file nhị phân.
    num_buffers : int
        Tổng số buffer khả dụng (>= 3).
    chunk_size : int
        Số phần tử đọc mỗi lần để tạo run ban đầu.

    Output
    ------
    In trực tiếp mảng đã sắp xếp.
    """

    if num_buffers < 3:
        raise ValueError("Cần ít nhất 3 buffer (1 input, 1 output, >=1 merge).")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Không tìm thấy file: {input_path}")

    temp_runs = []

    # =============================
    # Phase 1: Tạo sorted runs
    # =============================
    with open(input_path, "rb") as f:
        while True:
            chunk = read_doubles(f, chunk_size)
            if not chunk:
                break

            chunk.sort()

            temp_path = create_temp_file()
            with open(temp_path, "wb") as tf:
                write_doubles(tf, chunk)

            temp_runs.append(temp_path)

    # =============================
    # Phase 2: Multi-pass merge
    # =============================
    merge_width = num_buffers - 1

    while len(temp_runs) > 1:
        new_runs = []

        for i in range(0, len(temp_runs), merge_width):
            group = temp_runs[i:i + merge_width]

            heap = []
            file_ptrs = []

            for idx, path in enumerate(group):
                f = open(path, "rb")
                file_ptrs.append(f)
                value = read_doubles(f, 1)
                if value:
                    heapq.heappush(heap, (value[0], idx))

            temp_path = create_temp_file()
            with open(temp_path, "wb") as out:
                while heap:
                    smallest, file_idx = heapq.heappop(heap)
                    write_doubles(out, [smallest])

                    next_value = read_doubles(file_ptrs[file_idx], 1)
                    if next_value:
                        heapq.heappush(heap, (next_value[0], file_idx))

            for f in file_ptrs:
                f.close()

            new_runs.append(temp_path)

        for path in temp_runs:
            os.remove(path)

        temp_runs = new_runs

    # =============================
    # Phase 3: In kết quả
    # =============================
    if temp_runs:
        final_path = temp_runs[0]
        with open(final_path, "rb") as f:
            sorted_array = read_doubles(
                f,
                os.path.getsize(final_path) // DOUBLE_SIZE
            )

        print("Sorted result:")
        print(sorted_array)

        os.remove(final_path)
    else:
        print("File rỗng.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="External Merge Sort cho file .bin (double 8 bytes, little-endian)"
    )

    parser.add_argument(
        "input_path",
        type=str,
        nargs="?",
        default="utils/float64_50.bin",
        help="Đường dẫn tới file .bin (default: utils/float64_50.bin)"
    )

    parser.add_argument(
        "--buffers",
        type=int,
        default=4,
        help="Số buffer khả dụng (default=4)"
    )

    parser.add_argument(
        "--chunk",
        type=int,
        default=100000,
        help="Số phần tử mỗi run ban đầu (default=100000)"
    )

    args = parser.parse_args()

    external_merge_sort(
        input_path=args.input_path,
        num_buffers=args.buffers,
        chunk_size=args.chunk
    )