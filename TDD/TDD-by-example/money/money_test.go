package money

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestCasting(t *testing.T) {
	var a int64 = 10
	var b int = 10

	t.Run("primitive type castings", func(t *testing.T) {
		// 64 bit 환경으로 빌드하면 int는 64bit 이므로 기계어 수준에서는 비교 가능하다.
		// 하지만 강타입 언어라서 둘은 다른 타입으로 취급된다. 그래서 컴파일 실패한다.
		// assert.True(t, a == b)

		// primitive type은 둘을 서로 다른 한 쪽으로 변환해줘야 한다.
		assert.True(t, a == int64(b))
		assert.True(t, int(a) == b)
	})

	t.Run("type assertion", func(t *testing.T) {
		isInt := func(i any) bool {
			_, ok := i.(int)
			return ok
		}
		assert.False(t, isInt(a))
		assert.True(t, isInt(b))
	})
}

func TestCurrencyEquality(t *testing.T) {
	t.Run("cannot compare pointer and deep compare", func(t *testing.T) {
		// 아래 코드는 컴파일 실패한다. (golang은 강타입 언어라 비교 불가능하다.)
		// assert.False(t, NewDollar(5) == NewFranc(5))
		// assert.True(t, *NewDollar(5) == *NewFranc(5))

		// 타입을 직접 명시하지 않고, anonymous struct는 비교 가능하다
		assert.True(t, *NewDollar(5) == struct{ money }{money{5}})
		// 하지만 아래 포인터 주소 검사는 허용하지 않는다.
		// assert.False(t, NewDollar(5) == &struct{ money }{money{5}})
	})

	t.Run("compare by methods", func(t *testing.T) {
		assert.False(t, NewFranc(5).Equals(NewDollar(5)))
		assert.False(t, NewDollar(5).Equals(NewDollar(6)))
	})

	t.Run("testify equals", func(t *testing.T) {
		assert.NotEqual(t, NewFranc(5), NewDollar(5))
		assert.NotEqual(t, NewDollar(5), NewFranc(6))
	})
}

func TestCurrency(t *testing.T) {
	assert.Equal(t, "USD", NewDollar(1).Currency())
	assert.Equal(t, "CHF", NewFranc(1).Currency())
}
