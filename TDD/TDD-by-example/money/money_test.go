package money_test

import (
	"github.com/stretchr/testify/assert"
	"tddbe/money"
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
	t.Run("compare by methods", func(t *testing.T) {
		assert.False(t, money.NewFranc(5).Equals(money.NewDollar(5)))
		assert.False(t, money.NewDollar(5).Equals(money.NewDollar(6)))
	})

	t.Run("testify equals", func(t *testing.T) {
		assert.NotEqual(t, money.NewFranc(5), money.NewDollar(5))
		assert.NotEqual(t, money.NewDollar(5), money.NewFranc(6))
	})
}

func TestCurrency(t *testing.T) {
	assert.Equal(t, "USD", money.NewDollar(1).Currency())
	assert.Equal(t, "CHF", money.NewFranc(1).Currency())
}
