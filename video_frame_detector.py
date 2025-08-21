def find_missing_ranges(frames: list[int]) -> dict:
    if not frames:
        return {"gaps": [], "longest_gap": None, "missing_count": 0}
    
    max_frame = frames[0]
    for frame in frames:
        if frame > max_frame:
            max_frame = frame
    
    frame_set = set(frames)
    
    gaps = []
    missing_count = 0
    current_start = None
    
    for frame_num in range(1, max_frame + 1):
        if frame_num not in frame_set:
            if current_start is None:
                current_start = frame_num
            missing_count += 1
        else:
            if current_start is not None:
                gaps.append([current_start, frame_num - 1])
                current_start = None
    
    if current_start is not None:
        gaps.append([current_start, max_frame])
    
    longest_gap = None
    max_gap_length = 0
    
    for gap in gaps:
        gap_length = gap[1] - gap[0] + 1
        if gap_length > max_gap_length:
            max_gap_length = gap_length
            longest_gap = gap
    
    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }


if __name__ == "__main__":
    test_frames = [1, 2, 3, 5, 6, 10, 11, 16]
    result = find_missing_ranges(test_frames)
    print("Running the main example...")
    print(f"Frames received: {test_frames}")
    print(f"Analysis result: {result}")
    print()
    
    test_cases = [
        [1, 3, 5, 7, 9],
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8],
        [1],
        [1, 10],
        [5, 6, 7, 8, 9],
        []
    ]
    
    print("Testing some other scenarios:")
    for i, frames in enumerate(test_cases, 1):
        result = find_missing_ranges(frames)
        print(f"Scenario {i}: frames {frames}")
        print(f"  -> {result}")
        print()
