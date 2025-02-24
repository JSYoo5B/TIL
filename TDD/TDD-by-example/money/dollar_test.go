package money_test

import (
	"github.com/stretchr/testify/assert"
	"tddbe/money"
	"testing"
)

func TestDollarMultiplication(t *testing.T) {
	five := money.NewDollar(5)

	assert.True(t, money.NewDollar(10).Equals(five.Times(2)))
	assert.True(t, money.NewDollar(15).Equals(five.Times(3)))
}

func TestDollarEquality(t *testing.T) {
	t.Run("pointer compare and deep compare", func(t *testing.T) {
		assert.False(t, money.NewDollar(5) == money.NewDollar(5))
		assert.True(t, *money.NewDollar(5) == *money.NewDollar(5))
		assert.False(t, *money.NewDollar(5) == *money.NewDollar(6))
	})

	t.Run("compare by methods", func(t *testing.T) {
		assert.True(t, money.NewDollar(5).Equals(money.NewDollar(5)))
		assert.False(t, money.NewDollar(5).Equals(money.NewDollar(6)))
	})

	t.Run("testify supports deep compare", func(t *testing.T) {
		assert.Equal(t, money.NewDollar(5), money.NewDollar(5))
		assert.NotEqual(t, money.NewDollar(5), money.NewDollar(6))
	})
}

func TestDollarAddition(t *testing.T) {
	sum := money.NewDollar(5).Plus(money.NewDollar(5))

	assert.True(t, money.NewDollar(10).Equals(sum))
}
