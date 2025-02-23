package money_test

import (
	"github.com/stretchr/testify/assert"
	"tddbe/money"
	"testing"
)

func TestFrancMultiplication(t *testing.T) {
	five := money.NewFranc(5)

	assert.Equal(t, money.NewFranc(10), five.Times(2))
	assert.Equal(t, money.NewFranc(15), five.Times(3))
}

func TestFrancEquality(t *testing.T) {
	t.Run("compare by methods", func(t *testing.T) {
		assert.True(t, money.NewFranc(5).Equals(money.NewFranc(5)))
		assert.False(t, money.NewFranc(5).Equals(money.NewFranc(6)))
	})

	t.Run("testify supports deep compare", func(t *testing.T) {
		assert.Equal(t, money.NewFranc(5), money.NewFranc(5))
		assert.NotEqual(t, money.NewFranc(5), money.NewFranc(6))
	})
}
