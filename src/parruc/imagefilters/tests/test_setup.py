# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from parruc.imagefilters.testing import PARRUC_IMAGEFILTERS_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that parruc.imagefilters is properly installed."""

    layer = PARRUC_IMAGEFILTERS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if parruc.imagefilters is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'parruc.imagefilters'))

    def test_browserlayer(self):
        """Test that IParrucImagefiltersLayer is registered."""
        from parruc.imagefilters.interfaces import (
            IParrucImagefiltersLayer)
        from plone.browserlayer import utils
        self.assertIn(IParrucImagefiltersLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PARRUC_IMAGEFILTERS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['parruc.imagefilters'])

    def test_product_uninstalled(self):
        """Test if parruc.imagefilters is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'parruc.imagefilters'))

    def test_browserlayer_removed(self):
        """Test that IParrucImagefiltersLayer is removed."""
        from parruc.imagefilters.interfaces import IParrucImagefiltersLayer
        from plone.browserlayer import utils
        self.assertNotIn(IParrucImagefiltersLayer, utils.registered_layers())
