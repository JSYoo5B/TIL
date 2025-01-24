package vectorclock

func NewVectorClock(length int) VectorClock {
	return make([]int, length)
}

type VectorClock []int

func (v VectorClock) Copy() VectorClock {
	copied := make(VectorClock, len(v))
	copy(copied, v)
	return copied
}

func MergeClock(id int, prev, next VectorClock) VectorClock {
	if next == nil || len(prev) != len(next) {
		return prev
	}

	merged := prev.Copy()
	for idx := range len(prev) {
		if idx == id {
			continue
		}
		if prev[idx] > next[idx] {
			return prev
		} else if prev[idx] <= next[idx] {
			merged[idx] = next[idx]
		}
	}

	return merged
}
