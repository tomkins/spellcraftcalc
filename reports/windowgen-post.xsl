<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="DTD/xhtml1-strict.dtd" indent="yes" omit-xml-declaration="yes"/>
<xsl:template name="labeldef">
    <xsl:param name="uiwidth"/>
    <xsl:param name="uiposx"/>
    <xsl:param name="uiposy"/>
    <xsl:param name="uidata"/>
<LabelDef>
    <Color>
            <R>255</R>
            <G>255</G>
            <B>255</B>
            <A>255</A>
    </Color>
    <FontName>arial9</FontName>
    <xsl:choose>
    <xsl:when test="number($uiwidth) = -1">
    <Width><xsl:value-of select="string-length($uidata) * 15"/></Width>
    </xsl:when>
    <xsl:otherwise>
    <Width><xsl:copy-of select="$uiwidth"/></Width>
    </xsl:otherwise>
    </xsl:choose>
    <Height>16</Height>
    <MaxCharacters><xsl:value-of select="string-length($uidata) + 1"/></MaxCharacters>
    <Position>
            <X><xsl:copy-of select="$uiposx"/></X>
            <Y><xsl:copy-of select="$uiposy"/></Y>
    </Position>
    <Data><xsl:copy-of select="$uidata"/></Data>
</LabelDef>
</xsl:template>

<xsl:template match="/windowgen/label">
	<xsl:call-template name="labeldef">
		<xsl:with-param name="uiwidth"><xsl:value-of select="@width"/></xsl:with-param>
		<xsl:with-param name="uiposx"><xsl:value-of select="@x"/></xsl:with-param>
		<xsl:with-param name="uiposy" select="position() * 17"/>
		<xsl:with-param name="uidata"><xsl:value-of select="data"/></xsl:with-param>
	</xsl:call-template>
</xsl:template>
</xsl:stylesheet>


