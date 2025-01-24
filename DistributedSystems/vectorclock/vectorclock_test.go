package vectorclock

import (
	"fmt"
	"testing"
)

func TestVectorClock_Copy(t *testing.T) {
	clock1 := NewVectorClock(3)
	clock2 := clock1.Copy()

	if &clock1 == &clock2 {
		t.Fail()
	}
}

func TestMergeClock(t *testing.T) {
	testCases := map[string]struct {
		prev   VectorClock
		next   VectorClock
		id     int
		merged VectorClock
	}{
		"simple case": {
			prev:   VectorClock{1, 0, 0},
			next:   VectorClock{0, 2, 0},
			id:     1,
			merged: VectorClock{1, 2, 0},
		},
		"merging old clock": {
			prev:   VectorClock{1, 3, 0},
			next:   VectorClock{0, 2, 0},
			id:     1,
			merged: VectorClock{1, 3, 0},
		},
	}

	for name, tc := range testCases {
		t.Run(name, func(t *testing.T) {
			actual := MergeClock(tc.id, tc.prev, tc.next)
			fmt.Println(actual)
		})
	}
}
