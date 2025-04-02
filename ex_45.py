def mean(numbers):
    return sum(numbers) / len(numbers)

def standard_deviation(numbers):
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

if __name__ == '__main__':  # 메인 스크립트로 실행하면 출력, 모듈형식으로 임포트될 때는 미출력
    # 예제 데이터
    data = [10, 20, 30, 40, 50]

    # 결과 출력
    print("Mean:", mean(data))
    print("Standard Deviation:", standard_deviation(data))
    