# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import parruc.imagefilters


class ParrucImagefiltersLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=parruc.imagefilters)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'parruc.imagefilters:default')


PARRUC_IMAGEFILTERS_FIXTURE = ParrucImagefiltersLayer()


PARRUC_IMAGEFILTERS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PARRUC_IMAGEFILTERS_FIXTURE,),
    name='ParrucImagefiltersLayer:IntegrationTesting'
)


PARRUC_IMAGEFILTERS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PARRUC_IMAGEFILTERS_FIXTURE,),
    name='ParrucImagefiltersLayer:FunctionalTesting'
)


PARRUC_IMAGEFILTERS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PARRUC_IMAGEFILTERS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ParrucImagefiltersLayer:AcceptanceTesting'
)
