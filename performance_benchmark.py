import time
import random
from video_frame_detector import find_missing_ranges


def generate_test_data(size, missing_percentage=0.1):
    all_frames = list(range(1, size + 1))
    num_to_remove = int(size * missing_percentage)
    
    frames_to_remove = random.sample(all_frames, num_to_remove)
    test_frames = [f for f in all_frames if f not in frames_to_remove]
    
    return test_frames


def benchmark_solution():
    print("Let's see how fast this thing runs...")
    print("=" * 50)
    
    test_sizes = [100, 1000, 10000, 100000]
    missing_percentages = [0.05, 0.1, 0.2]
    
    for size in test_sizes:
        print(f"\nTesting with {size} frames:")
        print("-" * 30)
        
        for missing_pct in missing_percentages:
            test_frames = generate_test_data(size, missing_pct)
            expected_missing = int(size * missing_pct)
            
            start_time = time.time()
            result = find_missing_ranges(test_frames)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000
            
            actual_missing = result["missing_count"]
            is_correct = actual_missing == expected_missing
            
            print(f"With {missing_pct*100}% missing frames:")
            print(f"  Should find: {expected_missing} missing")
            print(f"  Actually found: {actual_missing} missing")
            print(f"  Took: {execution_time:.2f} ms")
            print(f"  Right answer? {'yep' if is_correct else 'nope'}")
            print(f"  Found {len(result['gaps'])} gaps")
            if result['longest_gap']:
                gap_size = result['longest_gap'][1] - result['longest_gap'][0] + 1
                print(f"  Biggest gap: {gap_size} frames")


def stress_test():
    print("\nNow let's really push it...")
    print("=" * 50)
    
    print("\nBig gap test:")
    frames = [1, 1000000]
    start_time = time.time()
    result = find_missing_ranges(frames)
    end_time = time.time()
    print(f"  Time: {(end_time - start_time)*1000:.2f} ms")
    print(f"  Missing: {result['missing_count']} frames")
    print(f"  Longest gap: {result['longest_gap']}")
    
    print("\nLots of small gaps:")
    frames = list(range(1, 10001, 2))
    start_time = time.time()
    result = find_missing_ranges(frames)
    end_time = time.time()
    print(f"  Time: {(end_time - start_time)*1000:.2f} ms")
    print(f"  Missing: {result['missing_count']} frames")
    print(f"  Gaps found: {len(result['gaps'])}")
    
    print("\nNo gaps at all:")
    frames = list(range(1, 10001))
    start_time = time.time()
    result = find_missing_ranges(frames)
    end_time = time.time()
    print(f"  Time: {(end_time - start_time)*1000:.2f} ms")
    print(f"  Missing: {result['missing_count']} frames")
    print(f"  Gaps found: {len(result['gaps'])}")


if __name__ == "__main__":
    random.seed(42)
    
    benchmark_solution()
    stress_test()
    
    print("\n" + "=" * 50)
    print("All done!")
